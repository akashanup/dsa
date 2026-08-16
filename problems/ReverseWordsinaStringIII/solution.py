"""
# Intuition
Instead of storing all space positions, we can process each word as soon as we find its end.

By maintaining the start index of the current word, we can reverse it immediately when encountering a space (or the end of the string), eliminating the need for an extra list of space indices.

# Approach
1. Convert the string into a character array.
2. Maintain a pointer `l` representing the start of the current word.
3. Iterate through the string:
   - When a space or the end of the string is reached, the current word spans from `l` to `i - 1`.
   - Reverse that segment using two pointers.
   - Update `l` to the start of the next word.
4. Convert the modified character array back into a string.

# Complexity
- Time complexity:
  - $$O(n)$$

  Each character is visited a constant number of times.

- Space complexity:
  - $$O(n)$$

  The character array created from the input string requires linear extra space.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        s = list(s)

        l = 0

        for i in range(n + 1):
            if i == n or s[i] == " ":
                r = i - 1

                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1

                l = i + 1

        