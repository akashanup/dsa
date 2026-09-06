"""
# Intuition
To group anagrams together, we need a way to identify strings that contain the same characters regardless of their order. If two strings are anagrams, sorting their characters will produce the same sequence. We can use this sorted representation as a unique key and group all strings sharing the same key.

# Approach
1. Create a hash map where:
   - Key = sorted version of the string (stored as a tuple).
   - Value = list of strings that belong to the same anagram group.
2. Iterate through each string in `strs`.
3. Sort the characters of the string and convert the result to a tuple so it can be used as a hashable dictionary key.
4. If the key does not exist in the hash map, initialize an empty list.
5. Append the current string to the corresponding list.
6. Return all grouped values from the hash map.

# Complexity
- Time complexity:
  - Sorting each string of length `k` takes `O(k log k)`.
  - For `n` strings, the overall time complexity is **O(n × k log k)**.

- Space complexity:
  - The hash map stores all input strings, resulting in **O(n × k)** space complexity.

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            sortedS = tuple(sorted(s))
            if sortedS not in hashmap:
                hashmap[sortedS] = []
            hashmap[sortedS].append(s)
        return list(hashmap.values())