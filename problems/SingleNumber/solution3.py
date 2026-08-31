"""
# Intuition
Since every element appears twice except one, we can count the frequency of each number using a hash map.

After counting all occurrences:
- Numbers that appear twice will have a frequency of `2`.
- The unique number will have a frequency of `1`.

We then iterate through the hash map and return the number whose frequency is `1`.

# Approach
1. Create an empty hash map `hashmap`.
2. Traverse the array and count the frequency of each number.
3. Iterate through the key-value pairs in the hash map.
4. Return the key whose frequency is equal to `1`.

This approach is straightforward and easy to understand, though it uses extra space to store frequencies.

# Complexity
- Time complexity:
  - `O(n)` because we traverse the array once to build the frequency map and once more to find the element with frequency `1`.

- Space complexity:
  - `O(n)` because the hash map may store up to `n` distinct elements.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 0
            hashmap[num] += 1

        for key, value in hashmap.items():
            if value == 1:
                return key
