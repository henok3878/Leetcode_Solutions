class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        i, j = 0, len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1 
            while not s[j].isalnum() and i < j:
                j -= 1 
            
            if s[i] != s[j]:
                return False 
            i += 1
            j -= 1 
        return True 