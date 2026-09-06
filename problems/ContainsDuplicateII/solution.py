"""
# Intuition

We need to determine whether the same number appears twice within a distance of at most `k`.

A hash map can help us store the most recent index where each number appeared. As we traverse the array, if we encounter a number that we've seen before, we calculate the distance between the current index and its previous occurrence. If that distance is less than or equal to `k`, we immediately return `True`.

# Approach

1. Create a hash map that stores the latest index of each number.
2. Traverse the array using `enumerate()`.
3. For each number:
   - Check if it already exists in the hash map.
   - If it does, compute the distance between the current index and the stored index.
   - If the distance is less than or equal to `k`, return `True`.
4. Update the hash map with the current index.
5. If no valid pair is found after traversing the entire array, return `False`.

# Complexity

- Time complexity:
  - $$O(n)$$
  - We traverse the array only once.

- Space complexity:
  - $$O(n)$$
  - In the worst case, every element is unique and stored in the hash map.

"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for idx, num in enumerate(nums):
            if num in hashmap:
                if idx - hashmap[num] <= k:
                    return True

            hashmap[num] = idx

        return False
