"""
# Intuition

Since we need to find the common strings with the minimum index sum, we can store the index of each string from `list1` in a hashmap for O(1) lookup. Then, while traversing `list2`, whenever we find a common string, we calculate its index sum and keep track of the minimum sum encountered so far. If a smaller sum is found, we update the answer list; if the sum matches the current minimum, we add the string to the result.

# Approach

1. Create a hashmap to store each string in `list1` along with its index.
2. Initialize:
   - `minSum` with a large value.
   - `ans` as an empty list.
3. Traverse `list2`.
4. For every string that exists in the hashmap:
   - Calculate the index sum.
   - If the sum is smaller than `minSum`, update `minSum` and reset `ans` with the current string.
   - If the sum is equal to `minSum`, append the current string to `ans`.
5. Return `ans`.

# Complexity

- Time complexity:
  - `O(n + m)`, where `n = len(list1)` and `m = len(list2)`

- Space complexity:
  - `O(n)` for storing the hashmap
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> Listhashmap = {}
        for i in range(len(list1)):
            if list1[i] not in hashmap:
                hashmap[list1[i]] = i

        minSum = 2000
        ans = []

        for i in range(len(list2)):
            if list2[i] in hashmap:
                tempMin = hashmap[list2[i]] + i

                if tempMin < minSum:
                    minSum = tempMin
                    ans = [list2[i]]
                elif tempMin == minSum:
                    ans.append(list2[i])

        return ans