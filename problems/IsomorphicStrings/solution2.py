"""
# Intuition

For two strings to be isomorphic, the mapping between characters must be one-to-one (bijective).

This means:
- A character in `s` must always map to the same character in `t`.
- A character in `t` must always come from the same character in `s`.

To enforce this, we maintain two hashmaps:
- `s_t` for mapping characters from `s` to `t`.
- `t_s` for mapping characters from `t` to `s`.

While traversing both strings, any inconsistency in either mapping means the strings are not isomorphic.

# Approach

1. Initialize two hashmaps:
   - `s_t` to store mappings from characters in `s` to characters in `t`.
   - `t_s` to store mappings from characters in `t` to characters in `s`.

2. Iterate through both strings simultaneously.

3. For each character pair `(si, ti)`:
   - If `si` has already been mapped and its mapped value is not `ti`, return `False`.
   - If `ti` has already been mapped and its mapped value is not `si`, return `False`.

4. Otherwise, store the mappings:
   - `si -> ti`
   - `ti -> si`

5. If the entire traversal completes without conflicts, return `True`.

# Complexity

- Time complexity:
  - `O(n)`

- Space complexity:
  - `O(k)`, where `k` is the number of distinct characters in the strings.

"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t = {}
        t_s = {}

        for i in range(len(s)):
            si = s[i]
            ti = t[i]

            if (si in s_t and s_t[si] != ti) or (ti in t_s and t_s[ti] != si):
                return False

            s_t[si] = ti
            t_s[ti] = si

        return True
