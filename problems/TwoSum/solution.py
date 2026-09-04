"""
# Intuition
The goal is to find two numbers whose sum equals the target while avoiding a brute-force comparison of every pair. As we iterate through the array, we can keep track of the numbers we've already seen in a hash map. For each number, we calculate the value needed to reach the target (`target - num`) and check if it has already been encountered.

# Approach
1. Initialize an empty hash map to store numbers and their indices.
2. Traverse the array using `enumerate`.
3. For each number:
   - Calculate the required complement (`balance = target - num`).
   - Check if the complement exists in the hash map.
   - If it exists, return the stored index of the complement and the current index.
   - Otherwise, store the current number and its index in the hash map.
4. Since the problem guarantees exactly one solution, the pair will be found during the traversal.

# Complexity

- Time complexity:
  - $$O(n)$$
  - We traverse the array once, and each hash map lookup/insertion takes $$O(1)$$ on average.

- Space complexity:
  - $$O(n)$$
  - In the worst case, we store all elements in the hash map.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> Listhashmap = {}

        for idx, num in enumerate(nums):
            balance = target - num

            if balance in hashmap:
                return [hashmap[balance], idx]

            hashmap[num] = idx
