"""
# Intuition
Each word is independent of the others. Since the problem only asks us to reverse the characters within each word while preserving the word order and spaces, we can process every word separately.

Python's slicing operation `[::-1]` provides a concise way to reverse a string, making it possible to solve the problem in a single line.

# Approach
1. Split the string into words using `split(" ")`.
2. Reverse each word using slicing `[::-1]`.
3. Join the reversed words back together using a single space.

# Complexity
- Time complexity:
  - $$O(n)$$

  Every character is visited once while reversing the words.

- Space complexity:
  - $$O(n)$$

  Additional space is used to store the reversed words and the final output string.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))