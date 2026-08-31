"""
# Intuition
Since every element appears exactly twice except one, we need a way to cancel out the duplicate numbers.

The XOR (`^`) operation has two useful properties:
- `a ^ a = 0`
- `a ^ 0 = a`

If we XOR all the numbers together, every duplicate pair cancels out, and only the single unique number remains.

# Approach
1. Initialize a variable `result = 0`.
2. Traverse the array.
3. XOR each number with `result`.
4. After processing all elements, `result` will contain the number that appears only once.
5. Return `result`.

This satisfies the requirement of linear time and constant extra space.

# Complexity
- Time complexity:
  - `O(n)` because we traverse the array once.

- Space complexity:
  - `O(1)` because only one extra variable is used.

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            result ^= nums[i]
        return result
