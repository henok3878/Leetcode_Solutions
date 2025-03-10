class Solution:
    def isPalindrome(self, s: str) -> bool:
        lr = [] 
        rl = [] 
        for ch in s:
            if ch.isalnum():
                ch = ch.lower()
                lr.append(ch) 
                rl.append(ch) 
        rl.reverse() 
        return lr == rl  