"""
# Intuition
We need to find the first occurrence of `needle` in `haystack`. A straightforward way is to try every possible starting position in `haystack` and check whether the characters match `needle` one by one. As soon as a complete match is found, return that starting index.

# Approach
- Let `n` and `m` be the lengths of `haystack` and `needle`.
- Iterate through every possible starting index `start` from `0` to `n - m`.
- For each `start`, compare characters of `needle` with the corresponding characters in `haystack`.
- Use a pointer `j` to track the number of matched characters.
- If all `m` characters match (`j == m`), return `start`.
- If no match is found after checking all possible positions, return `-1`.

# Complexity

- Time complexity:
  - $$O((n - m + 1) \cdot m)$$
  - In the worst case, we may compare up to `m` characters for each possible starting position.

- Space complexity:
  - $$O(1)$$
  - Only a few variables are used regardless of input size.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        for start in range(n - m + 1):
            j = 0

            while j < m and haystack[start + j] == needle[j]:
                j += 1

            if j == m:
                return start

        return -1