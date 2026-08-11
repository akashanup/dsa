"""
# Intuition

A common prefix cannot be longer than the shortest string in the array. So, instead of checking all possible characters across arbitrary lengths, we can use the shortest string as the candidate prefix and verify character by character whether every string contains the same character at the current position.

As soon as a mismatch is found, the prefix formed so far is the longest common prefix.

# Approach

1. Find the shortest string in the array since the answer cannot exceed its length.
2. Iterate through each character position of the shortest string.
3. For each position, compare the character with the corresponding character in every string.
4. If all strings have the same character, continue to the next position.
5. If a mismatch occurs, stop and return the prefix accumulated so far.
6. If all characters of the shortest string match, return the entire shortest string.

# Complexity

- Time complexity:

$$O(n \cdot m)$$

Where:
- \(n\) is the number of strings.
- \(m\) is the length of the shortest string.

In the worst case, every character of the shortest string is compared against all strings.

- Space complexity:

$$O(1)$$

Only a few variables are used regardless of the input size.
"""

class Solution:    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLenStr = min(strs, key=lambda x: len(x))
        i = 0
        while i < len(minLenStr):
            j = 0
            while j < len(strs) and strs[j][i] == minLenStr[i]:
                j +=  len(strs):
                break
            i += 1
        return minLenStr[:i]