class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        
        def helper(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i >= j:
                return int(i == j)
            res = 0 
            if s[i] == s[j]:
                res = 2 + helper(i + 1, j - 1) 
            else:
                res = max(helper(i, j - 1), helper(i + 1, j))
            dp[i][j] = res 
            return res
        
      
        dp = [[-1] * len(s) for _ in range(len(s))]
        return helper(0,len(s) - 1) 