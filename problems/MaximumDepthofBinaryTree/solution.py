"""
# Intuition

The maximum depth of a binary tree is the number of nodes along the longest path from the root to a leaf node.

For every node, the maximum depth depends on the deeper of its two subtrees. We can recursively compute the depth of the left and right subtrees, take the larger one, and add `1` for the current node.

# Approach

- If the current node is `None`, return `0`.
- Recursively calculate the depth of the left subtree.
- Recursively calculate the depth of the right subtree.
- Return:

```text
1 + max(leftDepth, rightDepth)
```

- The recursion continues until leaf nodes are reached and then propagates the maximum depth back up to the root.

# Complexity

- Time complexity:

$$O(n)$$

Each node is visited exactly once.

- Space complexity:

$$O(h)$$

Where `h` is the height of the tree due to the recursion call stack.

- Balanced tree: $$O(\log n)$$
- Skewed tree: $$O(n)$$

"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )
