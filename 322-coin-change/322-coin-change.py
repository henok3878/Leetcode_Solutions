class Solution:
    
   
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        m = 10**6
        dp = [-1] * (amount + 1)
        dp[0] = 0
        
        
        def helper(amt):
            if(amt < 0):
                return m 
            if(dp[amt] != -1):
                return dp[amt]
            
            res = m
            for c in coins:
                res = min(res,helper(amt - c))
            
            dp[amt] = res + 1
            return dp[amt]
        ret = helper(amount)
        return -1 if ret == (m + 1) else ret
    

"""

    minWays(11) = 1 + Min(minWays(10), minWays(9), minWays(6))

    
    -------------- n = 11
   '
   '
   '

    sum (nCk) for k in range(4)


"""