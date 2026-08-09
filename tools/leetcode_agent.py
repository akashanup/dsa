#!/usr/bin/env python3
"""Scaffold a new solved LeetCode problem inside this repository.

The script can work in two modes:
- manual: create the folder from a title you provide
- fetched: resolve a LeetCode problem or submission URL and pull the problem statement

In both modes it creates the problem folder, writes README.md and solution.py,
and updates the root README index.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
ROOT_README = ROOT / "README.md"
PROBLEM_ROOT = ROOT / "problems"
LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"


def _github_base_url() -> str:
    result = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    url = result.stdout.strip().removesuffix(".git")
    return f"{url}/tree/main/problems" if url else "https://github.com/akashanup/dsa/tree/main/problems"
LEETCODE_PROBLEM_URL = "https://leetcode.com/problems/{slug}/description/"
LEETCODE_URL_PATTERN = re.compile(r"https?://(?:www\.)?leetcode\.com/", re.I)
LEETCODE_SLUG_PATTERN = re.compile(r"/problems/([^/]+)/", re.I)


GRAPHQL_QUERY = """query questionData($titleSlug: String!) {
    question(titleSlug: $titleSlug) {
        questionFrontendId
        title
        content
        difficulty
        topicTags {
            name
        }
    }
}"""


@dataclass
class ProblemSpec:
    title: str
    folder: str
    problem_html: str | None
    section: str
    source_url: str | None
    problem_id: str | None
    difficulty: str | None
    topics: list[str] | None = None


def normalize_folder_name(title: str, folder: Optional[str]) -> str:
    if folder:
        return folder.strip().rstrip("/\\")

    cleaned = re.sub(r"\s+", "", title.strip())
    cleaned = re.sub(r"[^A-Za-z0-9-]", "", cleaned)
    return cleaned


def read_text(path: Optional[Path]) -> str | None:
    if path is None:
        return None
    return path.read_text(encoding="utf-8")


def looks_like_url(value: str) -> bool:
    return bool(LEETCODE_URL_PATTERN.match(value.strip()))


def extract_slug_from_url(value: str) -> str | None:
    match = LEETCODE_SLUG_PATTERN.search(value)
    if match:
        return match.group(1)
    return None


def fetch_problem_data(title_slug: str) -> dict[str, str]:
    payload = json.dumps(
        {
            "query": GRAPHQL_QUERY,
            "variables": {"titleSlug": title_slug},
        }
    ).encode("utf-8")
    request = Request(
        LEETCODE_GRAPHQL_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Origin": "https://leetcode.com",
            "Referer": LEETCODE_PROBLEM_URL.format(slug=title_slug),
        },
    )

    try:
        with urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8", errors="replace")
    except (HTTPError, URLError) as exc:
        raise RuntimeError(f"failed to fetch LeetCode problem data for '{title_slug}': {exc}") from exc

    parsed = json.loads(raw)
    question = parsed.get("data", {}).get("question")
    if not question:
        raise RuntimeError(f"LeetCode did not return problem data for '{title_slug}'")

    return {
        "id": str(question.get("questionFrontendId", "")),
        "title": str(question.get("title", "")).strip(),
        "content": str(question.get("content", "")).strip(),
        "difficulty": str(question.get("difficulty", "")).strip(),
        "topics": [t["name"] for t in question.get("topicTags", []) if isinstance(t, dict)],
    }


def strip_leading_title(source_text: str, title: str) -> str:
    lines = source_text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)

    if lines:
        first_line = lines[0].strip()
        normalized_first = re.sub(r"^#+\s*", "", first_line).strip().lower()
        if normalized_first == title.strip().lower():
            lines.pop(0)
            while lines and not lines[0].strip():
                lines.pop(0)

    return "\n".join(lines).strip()


def download_images(content_html: str, dest_dir: Path) -> str:
    """Download images referenced in HTML to images/ subdir and rewrite src attributes."""
    img_pattern = re.compile(r"""(<img[^>]*\bsrc=['"])([^'"]+)(['"][^>]*/?>)""", re.I)
    downloaded: dict[str, str] = {}
    images_dir = dest_dir / "images"

    def replace_src(match: re.Match[str]) -> str:
        prefix, src, suffix = match.group(1), match.group(2), match.group(3)
        if src in downloaded:
            return f"{prefix}{downloaded[src]}{suffix}"
        filename = re.sub(r"[?#].*$", "", src.split("/")[-1]) or "image"
        local_path = images_dir / filename
        try:
            req = Request(src, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(req, timeout=30) as resp:
                images_dir.mkdir(exist_ok=True)
                local_path.write_bytes(resp.read())
            rel = f"images/{filename}"
            downloaded[src] = rel
            return f"{prefix}{rel}{suffix}"
        except Exception as exc:
            print(f"warning: could not download image {src}: {exc}", file=sys.stderr)
            downloaded[src] = src
            return match.group(0)

    return img_pattern.sub(replace_src, content_html)


def html_to_markdown(content_html: str) -> str:
    def pre_block_replacer(match: re.Match[str]) -> str:
        code_block = match.group(1)
        code_block = re.sub(r"<[^>]+>", "", code_block)
        code_block = html.unescape(code_block).strip("\n")
        if not code_block:
            return "\n"
        return f"\n```text\n{code_block}\n```\n"

    def img_replacer(match: re.Match[str]) -> str:
        tag = match.group(0)
        src_m = re.search(r'src=[\'"](.*?)[\'"]', tag, re.I)
        alt_m = re.search(r'alt=[\'"](.*?)[\'"]', tag, re.I)
        src = src_m.group(1) if src_m else ""
        alt = alt_m.group(1) if alt_m else ""
        return f"![{alt}]({src})\n" if src else ""

    text = content_html
    text = re.sub(r"<pre[^>]*>(.*?)</pre>", pre_block_replacer, text, flags=re.I | re.S)
    text = re.sub(r"<img[^>]*/?>\s*", img_replacer, text, flags=re.I)
    text = re.sub(r"<br\\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<li[^>]*>", "- ", text, flags=re.I)
    text = re.sub(r"</li>", "\n", text, flags=re.I)
    text = re.sub(r"</?(ul|ol)[^>]*>", "\n", text, flags=re.I)
    text = re.sub(r"</p>", "\n\n", text, flags=re.I)
    text = re.sub(r"<p[^>]*>", "", text, flags=re.I)
    text = re.sub(r"<sup[^>]*>(.*?)</sup>", r"^\1", text, flags=re.I | re.S)
    text = re.sub(r"<(strong|b)[^>]*>", "**", text, flags=re.I)
    text = re.sub(r"</(strong|b)>", "**", text, flags=re.I)
    text = re.sub(r"<(em|i)[^>]*>", "*", text, flags=re.I)
    text = re.sub(r"</(em|i)>", "*", text, flags=re.I)
    text = re.sub(r"<code[^>]*>", "`", text, flags=re.I)
    text = re.sub(r"</code>", "`", text, flags=re.I)

    def anchor_replacer(match: re.Match[str]) -> str:
        href = match.group(1).strip()
        label = match.group(2).strip()
        return f"[{label}]({href})" if label else href

    text = re.sub(
        r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
        anchor_replacer,
        text,
        flags=re.I | re.S,
    )
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    text = text.replace("\xa0", " ")

    cleaned_lines: list[str] = []
    in_code_block = False
    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.strip().startswith("```"):
            marker = line.strip()
            cleaned_lines.append(marker)
            in_code_block = not in_code_block
            continue

        if in_code_block:
            cleaned_lines.append(line)
        else:
            cleaned_lines.append(line.strip())

    text = "\n".join(cleaned_lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def build_readme(
    title: str,
    problem_html: str | None,
    problem_id: str | None,
    difficulty: str | None,
    source_url: str | None,
) -> str:
    body = [f"# {title}", ""]

    metadata: list[str] = []
    if problem_id:
        metadata.append(f"- Problem: {problem_id}")
    if difficulty:
        metadata.append(f"- Difficulty: {difficulty}")
    if source_url:
        metadata.append(f"- Source: {source_url}")

    if metadata:
        body.extend(["## Metadata", "", *metadata, ""])

    if problem_html:
        markdown_problem = html_to_markdown(problem_html)
        body.extend(
            [
                "## Problem Statement",
                "",
                markdown_problem,
            ]
        )
    else:
        body.extend(
            [
                "## Problem Statement",
                "",
                "Paste the problem statement here.",
            ]
        )

    return "\n".join(body).rstrip() + "\n"


def write_problem_scaffold(spec: ProblemSpec) -> list[Path]:
    created_files: list[Path] = []
    problem_dir = PROBLEM_ROOT / spec.folder

    if problem_dir.exists():
        raise FileExistsError(f"Folder already exists: {problem_dir}")

    if not PROBLEM_ROOT.exists():
        raise FileNotFoundError(f"Problems folder not found: {PROBLEM_ROOT}")

    problem_dir.mkdir(parents=False, exist_ok=False)

    problem_html = spec.problem_html
    if problem_html:
        problem_html = download_images(problem_html, problem_dir)

    readme_path = problem_dir / "README.md"
    readme_text = build_readme(spec.title, problem_html, spec.problem_id, spec.difficulty, spec.source_url)
    readme_path.write_text(readme_text, encoding="utf-8")
    created_files.append(readme_path)

    solution_path = problem_dir / "solution.py"
    solution_path.write_text("", encoding="utf-8")
    created_files.append(solution_path)

    return created_files


def update_root_readme(readme_text: str, spec: ProblemSpec) -> str:
    section_heading = f"## {spec.section}"
    section_start = readme_text.find(section_heading)
    if section_start == -1:
        raise ValueError(f'Section "{spec.section}" was not found in {ROOT_README.name}.')

    next_section_start = readme_text.find("\n## ", section_start + len(section_heading))
    section_end = next_section_start if next_section_start != -1 else len(readme_text)

    section_block = readme_text[section_start:section_end]

    if re.search(rf"\[{re.escape(spec.title)}\]", section_block):
        return readme_text

    # Match data rows: lines starting with | number |
    data_row_pattern = re.compile(r"^\|\s*\d+\s*\|.+$", re.M)
    all_matches = list(data_row_pattern.finditer(section_block))
    if not all_matches:
        return readme_text

    # Parse rows into (title, full_row_text)
    title_from_row = re.compile(r"\|\s*\d+\s*\|\s*\[(.+?)\]")
    parsed_rows: list[tuple[str, str]] = []
    for m in all_matches:
        row_text = m.group(0)
        title_match = title_from_row.search(row_text)
        row_title = title_match.group(1) if title_match else ""
        parsed_rows.append((row_title, row_text))

    # Build new row
    github_link = f"{_github_base_url()}/{spec.folder}"
    difficulty = spec.difficulty or "-"
    topics = ", ".join(spec.topics) if spec.topics else "-"
    new_row = f"| 0 | [{spec.title}]({github_link}) | {difficulty} | {topics} |"
    parsed_rows.append((spec.title, new_row))

    # Sort alphabetically by title (case-insensitive)
    parsed_rows.sort(key=lambda x: x[0].lower())

    # Renumber 1..N
    renumbered = [
        re.sub(r"^\|\s*\d+\s*\|", f"| {i} |", row)
        for i, (_, row) in enumerate(parsed_rows, start=1)
    ]

    # Replace the entire rows block in the original text
    rows_start = section_start + all_matches[0].start()
    rows_end = section_start + all_matches[-1].end()
    updated = readme_text[:rows_start] + "\n".join(renumbered) + readme_text[rows_end:]
    return updated.rstrip() + "\n"


def ensure_parent_exists(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def finalize_problem(spec: ProblemSpec) -> list[Path]:
    problem_dir = PROBLEM_ROOT / spec.folder
    readme_path = problem_dir / "README.md"
    solution_path = problem_dir / "solution.py"

    if not problem_dir.exists():
        raise FileNotFoundError(f"Folder not found: {problem_dir}")
    if not readme_path.exists():
        raise FileNotFoundError(f"Missing README: {readme_path}")
    if not solution_path.exists():
        raise FileNotFoundError(
            f"Missing solution file: {solution_path}. Create it manually before step 2.",
        )

    root_text = ROOT_README.read_text(encoding="utf-8")
    updated_root = update_root_readme(root_text, spec)
    if updated_root != root_text:
        ROOT_README.write_text(updated_root, encoding="utf-8")

    return [ROOT_README]


def run_git_command(arguments: list[str]) -> str:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(arguments)} failed:\n{completed.stdout}{completed.stderr}"
        )
    return completed.stdout.strip()


def commit_and_push(spec: ProblemSpec, commit_message: str | None, push_enabled: bool) -> None:
    problem_dir = PROBLEM_ROOT / spec.folder
    run_git_command(["add", "README.md", f"problems/{spec.folder}"])

    diff_check = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=ROOT,
    )
    if diff_check.returncode == 0:
        print("No staged changes to commit.")
        return

    message = commit_message or spec.title
    run_git_command(["commit", "-m", message])

    if push_enabled:
        run_git_command(["push"])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a new LeetCode problem folder and update the repository index.",
    )
    parser.add_argument(
        "target",
        help="Problem title, problem URL, or submission URL.",
    )
    parser.add_argument(
        "--folder",
        help="Override the folder name. If omitted, it is derived from the title.",
    )
    parser.add_argument(
        "--source",
        type=Path,
        help="Optional text or markdown file with your own problem notes.",
    )
    parser.add_argument(
        "--section",
        default="Leetcode Problemset",
        help='Index section to update in the root README. Default: "Leetcode Problemset".',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing anything.",
    )
    parser.add_argument(
        "--step",
        choices=["1", "2"],
        default="1",
        help="Step 1 creates the problem folder; step 2 updates the index and pushes.",
    )
    parser.add_argument(
        "--commit-message",
        help="Custom commit message for step 2.",
    )
    parser.add_argument(
        "--no-push",
        action="store_true",
        help="Create the commit in step 2 without pushing it.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    target = args.target.strip()
    fetched_problem: dict[str, str] | None = None
    source_url: str | None = None

    if looks_like_url(target):
        slug = extract_slug_from_url(target)
        if not slug:
            print(
                "error: could not determine the LeetCode problem slug from the provided URL",
                file=sys.stderr,
            )
            return 1
        fetched_problem = fetch_problem_data(slug)
        source_url = target
        title = fetched_problem["title"]
    else:
        title = target

    folder = normalize_folder_name(title, args.folder)
    problem_dir = PROBLEM_ROOT / folder
    source_text = read_text(args.source)
    if source_text is not None:
        source_text = strip_leading_title(source_text, title)

    spec = ProblemSpec(
        title=title.strip(),
        folder=folder,
        problem_html=fetched_problem["content"] if fetched_problem else source_text,
        section=args.section.strip(),
        source_url=source_url,
        problem_id=fetched_problem["id"] if fetched_problem else None,
        difficulty=fetched_problem["difficulty"] if fetched_problem else None,
        topics=fetched_problem["topics"] if fetched_problem else None,
    )

    if args.dry_run:
        status = "already exists" if problem_dir.exists() else "would create"
        print(f"{status}: {problem_dir}")
        print(f"Would write: {problem_dir / 'README.md'}")
        if args.step == "2":
            print(f"Would update: {ROOT_README}")
        if fetched_problem:
            print(f"Fetched problem: {fetched_problem['id']}. {fetched_problem['title']} ({fetched_problem['difficulty']})")
            print(f"Source URL: {source_url}")
        return 0

    try:
        if args.step == "1":
            created_files = write_problem_scaffold(spec)
        else:
            created_files = finalize_problem(spec)
            commit_and_push(spec, args.commit_message, not args.no_push)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    for path in created_files:
        print(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
