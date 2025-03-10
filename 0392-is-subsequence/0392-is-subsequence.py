class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0 
        for ch in t:
            if si == len(s):
                return True 
            if ch == s[si]:
                si += 1 
 
        return si >= len(s)