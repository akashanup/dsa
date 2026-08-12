"""
# Intuition

Since the array is already sorted in non-decreasing order, we can use two pointers to efficiently find the pair whose sum equals the target. One pointer starts at the beginning of the array and the other at the end. Based on the current sum, we can decide which pointer to move:
- If the sum is too small, move the left pointer right to increase the sum.
- If the sum is too large, move the right pointer left to decrease the sum.
- If the sum matches the target, we have found the required pair.

This approach avoids checking every pair and uses the sorted property of the array.

# Approach

1. Initialize two pointers:
   - `s = 0` at the beginning of the array.
   - `e = len(numbers) - 1` at the end of the array.
2. While `s < e`:
   - Compute the sum of `numbers[s]` and `numbers[e]`.
   - If the sum equals the target, return their 1-indexed positions `[s + 1, e + 1]`.
   - If the sum is less than the target, move the left pointer right.
   - If the sum is greater than the target, move the right pointer left.
3. The problem guarantees exactly one solution, so the correct pair will always be found.

# Complexity

- Time complexity:
  - $$O(n)$$
  - Each pointer moves at most `n` times, so the array is traversed only once.

- Space complexity:
  - $$O(1)$$
  - Only two pointers are used, regardless of the input size.

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers) - 1

        while s < e:msSum = numbers[s] + numbers[e]

            if numsSum == target:
                return [s + 1, e + 1]
            elif numsSum < target:
                s += 1
            else:
                e -= 1