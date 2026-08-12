"""
# Intuition

Since the array is sorted, for every element `numbers[i]`, we only need to find its complement `target - numbers[i]` in the remaining portion of the array. Because the remaining elements are also sorted, Binary Search can efficiently locate the complement in `O(log n)` time.

By iterating through each element and performing a Binary Search on the subarray to its right, we can find the required pair while ensuring that the same element is not used twice.

# Approach

1. Create a helper function `binarySearch` that searches for a target value within a given range of indices.
2. Iterate through the array using index `i`.
3. For each element `numbers[i]`, calculate its complement:
   - `target - numbers[i]`
4. Use Binary Search on the portion of the array after index `i` (`i + 1` to `n - 1`) to find the complement.
5. If the complement is found, return the 1-indexed positions of the two numbers.

This approach leverages the sorted order of the array to reduce the search time for each element.

# Complexity

- Time complexity:
  - $$O(n \log n)$$
  - We iterate through the array once, and for each element perform a Binary Search that takes `O(log n)` time.

- Space complexity:
  - $$O(1)$$
  - Only a few variables are used, and no additional data structures are created.
"""

class Solution:
    def binarySearch(self, numbers, start, end, target):
        while start <= end:
            mid = start + ((end - start) // 2)

            if numbers[mid] == target:
                return mid
            elif numbers[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return None

    def twoSum(self, numbers: List[int], target: int) -> Listn = len(numbers)

        for i in range(n):
            counterPartIndex = self.binarySearch(
                numbers,
                i + 1,
                n - 1,
                target - numbers[i]
            )

            if counterPartIndex:
                return [i + 1, counterPartIndex + 1]