class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s) 
        m = len(p)

        @cache
        def helper(i, j):
            if j >= m:
                return i >= n
            
            if j + 1 < m and p[j + 1] == '*':
                res = helper(i , j + 2)
                if i < n:
                    curr = p[j] 
                    if curr == s[i] or curr == '.':
                        res = res or helper(i + 1, j) # choose 
                return res
            
            if i < n and (p[j] == s[i] or p[j] == '.'):
                return helper(i + 1, j + 1) 
            return False 
        
        return helper(0, 0)

                
        