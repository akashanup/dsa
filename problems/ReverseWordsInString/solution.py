"""
# Intuition
A straightforward way to reverse the order of words is to use the classic reverse-and-fix approach:

1. Reverse the entire string, which places the words in the desired order but also reverses each word.
2. Reverse each individual word to restore its original character order.

Before applying this technique, normalize the spaces by removing leading/trailing spaces and reducing multiple spaces between words to a single space.

# Approach
1. Normalize the input string using `" ".join(s.split())` so that:
   - Leading and trailing spaces are removed.
   - Multiple spaces between words are reduced to a single space.
2. Convert the string into a character array for in-place modifications.
3. Reverse the entire character array.
4. Traverse the array and reverse each word individually whenever a space (or the end of the array) is encountered.
5. Convert the character array back to a string and return it.

# Complexity
- Time complexity:
  - $$O(n)$$

  We traverse the string a constant number of times:
  - Space normalization: $$O(n)$$
  - Reverse entire string: $$O(n)$$
  - Reverse each word: $$O(n)$$

  Overall complexity remains $$O(n)$$.

- Space complexity:
  - $$O(n)$$

  The character array created from the normalized string requires linear extra space.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        sList = list(" ".join(s.split()))
        n = len(sList)

        # Reverse the entire string.
        for i in range(n // 2):
            sList[i], sList[n - i - 1] = sList[n - i - 1], sList[i]

        # Reverse each individual word.
        wordStart = 0

        for i in range(n + 1):
            if i == n or sList[i] == " ":
                left = wordStart
                right = i - 1

                while left < right:
                    sList[left], sList[right] = sList[right], sList[left]
                    left += 1
                    right -= 1

                wordStart = i + 1

        return "".join(sList)