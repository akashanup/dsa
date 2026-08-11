"""
# Intuition
We can simulate how binary addition is performed manually. Starting from the least significant bits (rightmost characters), we add the corresponding bits from both strings along with a carry from the previous position. The resulting bit is `sum % 2`, and the new carry is `sum // 2`.

# Approach
- Initialize two pointers `i` and `j` at the end of strings `a` and `b`.
- Maintain a `carry` variable initialized to `0`.
- Iterate while there are remaining digits in either string or a non-zero carry:
  - Add the current carry to a running `total`.
  - If `i` is valid, add the digit `a[i]` and decrement `i`.
  - If `j` is valid, add the digit `b[j]` and decrement `j`.
  - Append `total % 2` to the answer.
  - Update `carry = total // 2`.
- Since bits are added from right to left, reverse the collected result before returning it.

# Complexity
- Time complexity:
  - $$O(\max(n, m))$$

- Space complexity:
  - $$O(\max(n, m))$$
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        ans = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            ans.append(str(total % 2))
            carry = total // 2

        return ''.join(reversed(ans))