"""
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

Since the string needs to be reversed in-place with constant extra space, creating a new array is not allowed. We can use two pointers, one starting from the beginning and the other from the end of the array. By swapping the characters at these positions and moving the pointers toward each other, the string gets reversed without using extra memory.

# Approach
<!-- Describe your approach to solving the problem. -->

1. Initialize two pointers:
   - `l` at the start of the array (`0`)
   - `r` at the end of the array (`len(s) - 1`)
2. While `l < r`:
   - Swap `s[l]` and `s[r]`
   - Increment `l`
   - Decrement `r`
3. Continue until both pointers meet or cross.

This reverses the string directly within the given array.

# Complexity

- Time complexity:
  - $$O(n)$$
  - We traverse roughly half of the array, performing one swap per iteration.

- Space complexity:
  - $$O(1)$$
  - Only two pointers are used regardless of the input size.

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1