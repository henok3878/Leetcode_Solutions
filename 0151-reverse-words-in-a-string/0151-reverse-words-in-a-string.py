class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(' ') 
        words = [word for word in words if len(word)]
        words.reverse()
        return " ".join(words)