class Solution:
    def reverseWords(self, s: str) -> str:
        words = [] 
        curr = "" 
        for i in range(len(s)):
            if s[i] == ' ':
                if curr:
                    words.append(curr)
                curr = "" 
            else:
                curr += s[i]
        if curr:
            words.append(curr)
        words.reverse() 
        return " ".join(words)
        