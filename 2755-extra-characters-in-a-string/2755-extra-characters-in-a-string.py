class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words =set(dictionary) 
        n = len(s)
        @cache 
        def helper(idx):
            if idx >= n:
                return 0
            # don't use 
            mn = helper(idx + 1) + 1 

            # use 
            for i in range(idx, n):
                curr = s[idx: i + 1] 
                if curr in words:
                    mn = min(mn, helper(i + 1)) 
            
            return mn
        
        return helper(0)

