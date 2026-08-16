class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([_ for _ in s.split(" ") if _][::-1])