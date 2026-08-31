"""
# Intuition
Since every number appears exactly twice except one, we can keep track of numbers using a set.

- If a number is seen for the first time, add it to the set.
- If the same number appears again, remove it from the set.

After processing all elements, every duplicated number will have been added and removed once, leaving only the number that appears a single time in the set.

# Approach
1. Initialize an empty set `hashset`.
2. Traverse through each number in `nums`.
3. If the number is already in the set, remove it.
4. Otherwise, add it to the set.
5. After the traversal, the set will contain only the unique element.
6. Return that element using `pop()`.

# Complexity
- Time complexity:
  - `O(n)` because we iterate through the array once and set operations (`add`, `remove`, `in`) take `O(1)` on average.

- Space complexity:
  - `O(n)` in the worst case because the set can store up to all unique elements encountered during traversal.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()

        for num in nums:
            if num in hashset:
                hashset.remove(num)
            else:
                hashset.add(num)

        return hashset.pop()