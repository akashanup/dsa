"""
# Intuition

A Binary Search Tree is defined by its root. If we pick a value `i` as the root, then:

- All values smaller than `i` must belong to the left subtree.
- All values greater than `i` must belong to the right subtree.
- Every unique BST can therefore be formed by choosing each value in a range as the root and recursively generating all possible left and right subtrees.

The idea is to generate all valid BSTs for a given range `[start, end]` and combine every possible left subtree with every possible right subtree.

# Approach

1. Create a recursive function `createTrees(start, end)` that returns all unique BSTs that can be formed using values in the range `[start, end]`.
2. If `start > end`, return `[None]` to represent an empty subtree.
3. Iterate through every value `i` in the range and treat it as the root.
4. Recursively generate:
   - All possible left subtrees using values `[start, i-1]`.
   - All possible right subtrees using values `[i+1, end]`.
5. Combine every left subtree with every right subtree by attaching them to a new root node `i`.
6. Store all generated trees and return them.
7. Start the recursion with the range `[1, n]`.

# Complexity

- Time complexity:

$$O(C_n \cdot n)$$

Where \(C_n\) is the \(n^{th}\) Catalan number. Since every unique BST must be constructed and returned, the runtime is proportional to the number of generated trees.

- Space complexity:

$$O(C_n \cdot n)$$

For storing all generated BSTs and the recursive call stack.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def createTrees(self, start, end):
        if start > end:
            return [None]

        trees = []

        for i in range(start, end + 1):
            leftSubTrees = self.createTrees(start, i - 1)
            rightSubTrees = self.createTrees(i + 1, end)

            for left in leftSubTrees:
                for right in rightSubTrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    trees.append(root)

        return trees

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.createTrees(1, n)