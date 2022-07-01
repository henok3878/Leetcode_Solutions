class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        last = -1 
        for c in s:
            found = False
            for i in range(last + 1,len(t)):
                c2 = t[i]
                if c == c2:
                    last = i
                    found = True 
                    break
            if not found:
                return False 
        return True 