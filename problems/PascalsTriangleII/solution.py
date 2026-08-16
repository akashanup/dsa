"""
# Intuition
Pascal's Triangle can be built row by row. Each element in a row (except the first and last) is the sum of the two adjacent elements from the previous row.

Starting from the second row `[1, 1]`, we repeatedly generate the next row using the current row until we reach the required `rowIndex`.

# Approach
1. Handle the edge case where `rowIndex = 0` by returning `[1]`.
2. Initialize `currentRow` as `[1, 1]`, which represents row 1.
3. For each row from `2` to `rowIndex`:
   - Create a new row starting with `1`.
   - For every adjacent pair in `currentRow`, append their sum to the new row.
   - Append a trailing `1` to complete the row.
   - Update `currentRow` to this newly generated row.
4. Return `currentRow` after all rows have been generated.

# Complexity
- Time complexity:
  - $$O(n^2)$$

  Generating the `i`-th row requires processing `i-1` elements. The total work is:

  $$1 + 2 + 3 + \cdots + n = O(n^2)$$

  where `n = rowIndex`.

- Space complexity:
  - $$O(n)$$

  We only store the current row being generated, whose size is at most `rowIndex + 1`.

"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
                
        currentRow = [1, 1]
        for i in range(2, rowIndex + 1):
            nextRow = [1]
            for j in range(i - 1):
                nextRow.append(currentRow[j] + currentRow[j + 1])
            nextRow.append(1)
            currentRow = nextRow
        
        return currentRow