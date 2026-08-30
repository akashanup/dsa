"""
# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

If an element appears more than once, we need a fast way to determine whether we have already seen it before. A hash set provides constant-time lookup on average, making it ideal for tracking previously encountered elements. As we iterate through the array, if a number is already present in the set, we immediately know a duplicate exists.

# Approach
<!-- Describe your approach to solving the problem. -->

1. Create an empty hash set.
2. Traverse the array one element at a time.
3. For each number:
   - Check if it already exists in the hash set.
   - If it does, return `True` since a duplicate has been found.
   - Otherwise, add the number to the hash set.
4. If the traversal completes without finding any duplicate, return `False`.

This approach allows us to detect duplicates efficiently in a single pass through the array.

# Complexity

- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

We iterate through the array once, and each hash set lookup and insertion takes $$O(1)$$ on average.

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

$$O(n)$$

In the worst case, all elements are distinct, so the hash set stores all $$n$$ elements.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set([])

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)

        return False
