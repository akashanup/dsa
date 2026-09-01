"""
# Intuition

The problem requires returning only the unique elements that appear in both arrays. A hash set is a natural choice because it provides O(1) average-time lookups. By storing the elements of one array in a set, we can efficiently check whether elements from the other array exist in it.

To avoid duplicates in the result, once an element is found in both arrays and added to the answer, it is removed from the set. This guarantees that each common element is added only once.

# Approach

1. Swap the arrays if `nums1` is larger than `nums2` so that the hash set is built from the smaller array, reducing auxiliary space usage.
2. Insert all elements from `nums1` into a hash set.
3. Traverse `nums2`:
   - If the current element exists in the hash set, add it to the result.
   - Remove it from the hash set to ensure it cannot be added again.
4. Return the result list.

# Complexity

- Time complexity:
  - Building the hash set takes `O(min(n, m))`.
  - Traversing the other array takes `O(max(n, m))`.
  - Overall: **O(n + m)**

- Space complexity:
  - The hash set stores at most the elements of the smaller array.
  - Overall: **O(min(n, m))**

"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, numsset = set([])

        for num in nums1:
            hashset.add(num)

        intersectionList = []

        for num in nums2:
            if num in hashset:
                intersectionList.append(num)
                hashset.remove(num)

        return intersectionList