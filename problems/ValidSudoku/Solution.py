"""
# Intuition
A valid Sudoku board must satisfy three independent conditions:
1. Each row should not contain duplicate digits.
2. Each column should not contain duplicate digits.
3. Each 3×3 sub-box should not contain duplicate digits.

Since only the filled cells need validation, we can use a set to track the digits already seen while traversing a row, column, or sub-box. If a digit is encountered again within the same row, column, or sub-box, the board is invalid.

# Approach
1. Traverse each row and use a set to check for duplicate digits.
2. Traverse each column and use a set to check for duplicate digits.
3. Traverse each 3×3 sub-box:
   - Iterate through the starting coordinates of each sub-box using `(0, 3, 6)`.
   - Use a set to keep track of digits seen in the current sub-box.
   - If a duplicate digit is found, return `False`.
4. If all rows, columns, and sub-boxes are valid, return `True`.

# Complexity
- Time complexity:
  - $$O(9 \times 9 + 9 \times 9 + 9 \times 9) = O(243)$$
  - Since the board size is fixed (9×9), this simplifies to **$$O(1)$$**.

- Space complexity:
  - $$O(9)$$ for the set used during row, column, or sub-box validation.
  - Since the board size is fixed, this simplifies to **$$O(1)$$**.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            rowSet = set()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in rowSet:
                        return False
                    rowSet.add(board[r][c])

        for c in range(9):
            columnSet = set()
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] in columnSet:
                        return False
                    columnSet.add(board[r][c])

        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):

                subBoxSet = set()

                for r in range(boxRow, boxRow + 3):
                    for c in range(boxCol, boxCol + 3):

                        if board[r][c] == ".":
                            continue

                        if board[r][c] in subBoxSet:
                            return False

                        subBoxSet.add(board[r][c])

        return True