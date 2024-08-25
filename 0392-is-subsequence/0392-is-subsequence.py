class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0  
        n = len(t)
        last = len(s) - 1
        if last < 0:
            return True 
        for i in range(n-1,-1,-1):
            ch = s[last] 
            if (t[i] == ch):
                last -= 1
            if last < 0:
                return True 
        return False 


