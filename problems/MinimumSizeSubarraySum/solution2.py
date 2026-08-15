"""
# Intuition

Since all elements in the array are positive, the prefix sum array is strictly increasing. This allows us to use binary search to efficiently find the smallest ending index for each starting index such that the subarray sum is at least `target`.

For every index `i`, we want to find the first index `j` where:

```text
prefix[j] - prefix[i] >= target
```

which can be rewritten as:

```text
prefix[j] >= prefix[i] + target
```

Since the prefix array is sorted, we can use binary search to find this index.

# Approach

1. Build a prefix sum array `prefix` where:
   - `prefix[i]` stores the sum of the first `i` elements.
2. For each starting index `i`:
   - Compute the required prefix sum value:
     ```python
     required = prefix[i] + target
     ```
   - Use binary search on the prefix sum array to find the first index `j` such that:
     ```python
     prefix[j] >= required
     ```
   - Update the minimum length using:
     ```python
     j - i
     ```
3. If no valid subarray is found, return `0`; otherwise return the minimum length found.

# Complexity

- Time complexity:
  - `O(n log n)`
  - Building the prefix sum array takes `O(n)`.
  - Performing binary search for each index takes `O(log n)`.
  - Total: `O(n log n)`.

- Space complexity:
  - `O(n)` for the prefix sum array.
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        minLen = n + 1

        for i in range(n):
            required = prefix[i] + target

            left, right = i + 1, n

            while left <= right:
                mid = left + (right - left) // 2

                if prefix[mid] >= required:
                    right = mid - 1
                else:
                    left = mid + 1

            if left <= n:
                minLen = min(minLen, left - i)

        return 0 if minLen == n + 1 else minLen