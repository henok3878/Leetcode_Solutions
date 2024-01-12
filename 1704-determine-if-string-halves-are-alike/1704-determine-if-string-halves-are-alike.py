class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower() 
        n = len(s) 
        half = n//2 
        vowels = ["a","e","i","o","u"] 
        cnt_a = 0 
        cnt_b = 0 
        for i in range(n):
            if s[i] in vowels:
                if i < half:
                    cnt_a += 1 
                else:
                    cnt_b += 1 
        return cnt_a == cnt_b 