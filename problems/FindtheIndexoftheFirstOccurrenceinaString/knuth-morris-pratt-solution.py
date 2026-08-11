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
    def computeLPS(self, pattern, lps):
        i = 0
        j = 1
        while j < len(pattern):
            if pattern[i] == pattern[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i-1]
                    
        
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        self.computeLPS(needle, lps)
        
        h, n = 0, 0
        while h < len(haystack):
            if haystack[h] == needle[n]:
                h += 1
                n += 1
            if n == len(needle):
                return h-n
            if h < len(haystack) and haystack[h] != needle[n]:
                if n > 0:
                    n = lps[n-1]
                else:
                    h += 1
        return -1