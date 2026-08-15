"""
# Intuition

Since all numbers in the array are positive, expanding a window always increases (or maintains) the sum, and shrinking it always decreases the sum. This property makes the sliding window technique ideal for finding the smallest subarray whose sum is at least `target`.

# Approach

1. Use two pointers, `left` and `right`, to maintain a sliding window.
2. Expand the window by moving `right` and adding `nums[right]` to the current sum.
3. Whenever the current sum becomes greater than or equal to `target`:
   - Update the minimum length using the current window size.
   - Shrink the window from the left to see if a smaller valid subarray exists.
4. Continue until the entire array has been processed.
5. If no valid subarray is found, return `0`.

# Complexity

- Time complexity:
  - `O(n)` because each element is added to and removed from the window at most once.

- Space complexity:
  - `O(1)` since only a few variables are used.

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currSum = 0
        minLen = float("inf")

        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target:
                minLen = min(minLen, right - left + 1)
                currSum -= nums[left]
                left += 1

        return 0 if minLen == float("inf") else minLen