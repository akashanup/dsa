"""
# Alternative Approach: Sliding Window + Hash Set

Instead of storing indices, we can maintain a sliding window of size `k`.

## Approach

1. Maintain a set containing at most the last `k` elements.
2. Traverse the array.
3. Before inserting the current element:
   - If it already exists in the set, return `True`.
4. Add the current element to the set.
5. If the window size exceeds `k`, remove the element that falls out of the window.
6. If no duplicate is found, return `False`.

## Complexity

- Time complexity:
  - $$O(n)$$

- Space complexity:
  - $$O(\min(n, k))$$

"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            if len(window) > k:
                window.remove(nums[i - k])

        return False