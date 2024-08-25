class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() 
        rev_s = "" 
        for c in s:
            if c.isalnum():
                rev_s += c 
        return  rev_s == rev_s[::-1]