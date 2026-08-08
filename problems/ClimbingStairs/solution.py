"""
# Intuition

At each step `n`, there are only two possible ways to reach it:

1. Take **1 step** from step `n - 1`
2. Take **2 steps** from step `n - 2`

This gives the recurrence relation:

```text
ways(n) = ways(n - 1) + ways(n - 2)
```

A naive recursive solution would recompute the same subproblems many times. To avoid this, we store already computed results in a hashmap (memoization) so that each state is calculated only once.

# Approach

- Create a recursive helper function that returns the number of ways to reach step `n`.
- If `n <= 2`, return `n` as the base case.
- Use a hashmap to cache previously computed results.
- Before computing `helper(n)`, check whether it already exists in the hashmap.
- If not, recursively compute:
  
```text
helper(n) = helper(n-1) + helper(n-2)
```

- Store the result in the hashmap and return it.
- Start the recursion with an empty hashmap.

# Complexity

- Time complexity:

$$O(n)$$

Each state from `1` to `n` is computed only once and then reused from the hashmap.

- Space complexity:

$$O(n)$$

- `O(n)` for the memoization hashmap.
- `O(n)` recursive call stack in the worst case.
"""

class Solution:
    def helper(self, n, hashmap):
        if n <= 2:
            return n

        if n not in hashmap:
            hashmap[n] = self.helper(n - 1, hashmap) + self.helper(n - 2, hashmap)

        return hashmap[n]

    def climbStairs(self, n: int) -> int:
        return self.helper(n, {})
