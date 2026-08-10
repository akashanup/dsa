"""
# Intuition

A full binary tree can only have an odd number of nodes because every node must have either 0 or 2 children. For a tree with `n` nodes, we can pick an odd number of nodes for the left subtree and assign the remaining `n - i - 1` nodes to the right subtree (subtracting 1 for the root). Both subtrees must also be full binary trees.

Since the same subtree sizes are computed repeatedly, we use memoization to cache and reuse previously generated trees.

# Approach

1. Use a recursive helper function that returns all possible full binary trees with `n` nodes.
2. If `n` is even, return an empty list since a full binary tree cannot have an even number of nodes.
3. If `n == 1`, return a single-node tree.
4. Check the memoization dictionary before computing a result.
5. For every odd split `i`:
   - Generate all full binary trees with `i` nodes for the left subtree.
   - Generate all full binary trees with `n - i - 1` nodes for the right subtree.
   - Combine every left tree with every right tree under a new root node.
6. Store the generated trees in the memo table and return them.

# Complexity

- Time complexity:

  $$O(F(n))$$

  where `F(n)` is the number of full binary trees with `n` nodes. Since every valid tree must be generated, the output size dominates the complexity.

- Space complexity:

  $$O(F(n))$$

  for storing memoized results and all generated trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, n, lookup):
        if n in lookup:
            return lookup[n]

        if n % 2 == 0:
            return []

        if n == 1:
            lookup[n] = [TreeNode(0)]
            return lookup[n]

        fbts = []

        for i in range(1, n, 2):
            left = self.helper(i, lookup)
            right = self.helper(n - i - 1, lookup)

            for l in left:
                for r in right:
                    fbts.append(TreeNode(0, l, r))

        lookup[n] = fbts
        return lookup[n]

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(n, {})
