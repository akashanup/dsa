"""
# Intuition
The naive approach may compare the same characters multiple times after a mismatch. The Knuth-Morris-Pratt (KMP) algorithm avoids these redundant comparisons by preprocessing `needle`.

We build an **LPS (Longest Prefix Suffix)** array, where `lps[i]` stores the length of the longest proper prefix of `needle[0...i]` that is also a suffix.

When a mismatch occurs after some characters have already matched, the LPS array tells us where to continue matching in `needle` without moving backward in `haystack`.

# Approach

### 1. Compute the LPS array

- Initialize `lps` with zeroes.
- Use `l` to track the length of the current longest proper prefix that is also a suffix.
- Start from index `1`, since `lps[0]` is always `0`.
- If `pat[i] == pat[l]`:
  - Increment `l`.
  - Set `lps[i] = l`.
  - Move `i` forward.
- If the characters do not match:
  - If `l > 0`, update `l` to `lps[l - 1]` and try again.
  - Otherwise, set `lps[i] = 0` and move `i` forward.

### 2. Search using KMP

- Use `i` to traverse `haystack` and `j` to traverse `needle`.
- If `haystack[i] == needle[j]`, increment both pointers.
- If `j` reaches the length of `needle`, the complete pattern has matched. Return `i - j`.
- On a mismatch:
  - If `j > 0`, set `j = lps[j - 1]`.
  - Otherwise, increment `i`.
- If the search finishes without a full match, return `-1`.

# Complexity

- Time complexity:
  - $$O(n + m)$$
  - Computing the LPS array takes `O(m)`.
  - Searching through `haystack` takes `O(n)`.

- Space complexity:
  - $$O(m)$$
  - The LPS array stores one value for each character in `needle`.

"""

class Solution:
    def computeLPS(self, pat, lps):
        l = 0
        lps[0] = 0
        i = 1

        while i < len(pat):
            if pat[i] == patl += 1
                lps[i] = l
                i += 1
            else:
                if l > 0:
                    l = lps[l - 1]
                else:
                    lps[i] = 0
                    i += 1

    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        self.computeLPS(needle, lps)

        i, j = 0, 0

        while i < len(haystack):
            if haystack[i] == needlei += 1
                j += 1

            if j == len(needle):
                return i - j
            elif i < len(haystack) and haystack[i] != needleif j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1