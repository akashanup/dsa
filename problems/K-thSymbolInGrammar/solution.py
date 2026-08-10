"""
# Intuition

If we write out the first few rows:

```text
n = 1      0
n = 2     0 | 1
n = 3    01 | 10
n = 4  0110 | 1001
```

A clear pattern emerges:

- The left half of every row is exactly the previous row.
- The right half is the bitwise complement of the left half.

For example, in the 4th row:

```text
0110 | 1001
```

The right half (`1001`) is the complement of the left half (`0110`).

If the row length is `L` and `mid = L / 2`, then for every position `i` in the left half:

```text
value[mid + i] = 1 - value[i]
```

Example for row 4:

```text
index : 1 2 3 4 | 5 6 7 8
value : 0 1 1 0 | 1 0 0 1

value[5] = 1 - value[1]
value[6] = 1 - value[2]
value[7] = 1 - value[3]
value[8] = 1 - value[4]
```

Therefore:

- If `k` lies in the left half, we simply need the `k`th value from the previous row.
- If `k` lies in the right half, we find the corresponding position in the left half (`k - mid`) and take its complement.

This naturally leads to a recursive solution.

# Approach

Let the length of the `n`th row be:

```text
2^(n-1)
```

and let:

```text
mid = length / 2
```

For any row:

```text
left half  = (n-1)th row
right half = complement of left half
```

Now consider the position `k`:

### Case 1: `k <= mid`

The position lies in the left half.

Since the left half is exactly the previous row, the answer is:

```text
kthGrammar(n-1, k)
```

### Case 2: `k > mid`

The position lies in the right half.

The corresponding index in the left half is:

```text
k - mid
```

Since the right half is the complement of the left half, the answer is:

```text
1 - kthGrammar(n-1, k-mid)
```

### Recurrence

```text
kthGrammar(n, k) =
    kthGrammar(n-1, k)                 if k <= mid
    1 - kthGrammar(n-1, k-mid)         otherwise
```

Base case:

```text
kthGrammar(1, 1) = 0
```

# Complexity

- Time complexity:

$$O(n)$$

Only one recursive call is made at each level.

- Space complexity:

$$O(n)$$

Due to the recursion stack.
"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        nThRowDigitCount = 2 ** (n - 1)
        mid = nThRowDigitCount // 2

        if k <= mid:
            return self.kthGrammar(n - 1, k)

        return 1 - self.kthGrammar(n - 1, k - mid)