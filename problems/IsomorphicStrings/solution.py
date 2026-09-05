"""
# Intuition

For two strings to be isomorphic, each character in `s` must map to exactly one character in `t`, and no two different characters in `s` can map to the same character in `t`.

We maintain:
- A hashmap `s_t` to store the mapping from characters in `s` to characters in `t`.
- A set `t_set` to keep track of characters in `t` that have already been mapped.

While traversing both strings:
- If a character from `s` has not been seen before, its corresponding character in `t` must not already be mapped to another character.
- If a character from `s` has been seen before, it must map to the same character in `t` as before.

If any of these conditions are violated, the strings are not isomorphic.

# Approach

1. Initialize an empty hashmap `s_t` and an empty set `t_set`.
2. Traverse both strings character by character.
3. For each pair `(si, ti)`:
   - If `si` is not in `s_t` but `ti` already exists in `t_set`, return `False`.
   - If `si` already exists in `s_t` and its mapped value is different from `ti`, return `False`.
4. Otherwise, store/update the mapping `si -> ti` and add `ti` to `t_set`.
5. If the entire traversal completes without conflicts, return `True`.

# Complexity

- Time complexity:
  - `O(n)`

- Space complexity:
  - `O(k)`, where `k` is the number of distinct characters in `s` (at most the size of the character set).

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_set = set([])

        for i in range(len(s)):
            si = s[i]
            ti = t[i]

            if (si not in s_t and ti in t_set) or (si in s_t and s_t[si] != ti):
                return False

            s_t[si] = ti
            t_set.add(ti)

        return True