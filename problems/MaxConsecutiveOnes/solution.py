"""
# Intuition

We need to find the longest contiguous sequence of `1`s in the array.

While traversing the array, keep track of the current streak of consecutive `1`s. Whenever a `0` is encountered, the streak ends, so update the maximum streak seen so far and reset the current streak. After the traversal, perform one final update to handle the case where the array ends with consecutive `1`s.

# Approach

1. Initialize two variables:
   - `currOnes` to store the length of the current consecutive sequence of `1`s.
   - `maxOnes` to store the maximum sequence length found so far.
2. Iterate through the array:
   - If the current element is `1`, increment `currOnes`.
   - If the current element is `0`:
     - Update `maxOnes` with the larger of `maxOnes` and `currOnes`.
     - Reset `currOnes` to `0`.
3. After the loop, update `maxOnes` one final time to account for a sequence of `1`s ending at the last element.
4. Return `maxOnes`.

# Complexity

- Time complexity:
  - `O(n)` since we traverse the array exactly once.

- Space complexity:
  - `O(1)` since only a constant amount of extra space is used.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currOnes = 0

        for num in nums:
            if num == 0:
                maxOnes = max(maxOnes, currOnes)
                currOnes = 0
            else:
                currOnes += 1

        maxOnes = max(maxOnes, currOnes)
        return maxOnes