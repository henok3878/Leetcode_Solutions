class Solution:
    def reverseWords(self, s: str) -> str:
        words = [] 
        n = len(s) 
        i = 0 
        while i < n: 
            j = i
            while j < n and s[j] != ' ':
                j += 1 
            if j > i:
                words.append(s[i:j]) 
            i = j + 1
        return " ".join(reversed(words))