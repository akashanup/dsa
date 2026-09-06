"""
# Intuition

To find the first non-repeating character, we first need to know how many times each character appears in the string. Once we have the frequency of every character, we can scan the string from left to right and return the index of the first character whose frequency is exactly `1`.

# Approach

1. Create a hash map to store the frequency of each character.
2. Traverse the string and count the occurrences of every character.
3. Traverse the string again using `enumerate()`.
4. For each character, check its frequency in the hash map.
5. Return the index of the first character whose frequency is `1`.
6. If no such character exists, return `-1`.

# Complexity

- Time complexity:
  - $$O(n)$$
  - One pass to build the frequency map and another pass to find the first unique character.

<br>

- Space complexity:
  - $$O(k)$$
  - Where `k` is the number of distinct characters in the string. In this problem, since only lowercase English letters are allowed, `k ≤ 26`, making the space effectively constant.

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for ch in s:
            if ch not in hashmap:
                hashmap[ch] = 0
            hashmap[ch] += 1

        for idx, ch in enumerate(s):
            if hashmap[ch] == 1:
                return idx

        return -1