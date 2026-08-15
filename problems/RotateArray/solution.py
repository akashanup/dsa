"""
# Intuition

A right rotation by `k` positions can be achieved efficiently using array reversals instead of shifting elements one at a time.

The key observation is that after reversing the entire array, the elements that should appear at the beginning of the rotated array are moved to the front, but in reverse order. Reversing the first `k` elements and then the remaining `n-k` elements restores the correct ordering within both parts.

# Approach

1. Compute `k %= n` to handle cases where `k` is greater than the array length.
2. Reverse the entire array.
3. Reverse the first `k` elements.
4. Reverse the remaining elements from index `k` to `n-1`.

Example:

```text
nums = [1,2,3,4,5,6,7], k = 3

Reverse entire array:
[7,6,5,4,3,2,1]

Reverse first k elements:
[5,6,7,4,3,2,1]

Reverse remaining elements:
[5,6,7,1,2,3,4]
```

This rotates the array in-place without using any extra space.

# Complexity

- Time complexity:

$$O(n)$$

The array is traversed a constant number of times while performing the three reversals.

- Space complexity:

$$O(1)$$

All operations are performed in-place using only a few variables.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        n = len(nums)

        for i in range(n // 2):
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]

        i, j = 0, k - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        i, j = k, n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
```