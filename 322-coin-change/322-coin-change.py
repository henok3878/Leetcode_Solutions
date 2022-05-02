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
                res = min(res,helper(amt - c) + 1)
            
            dp[amt] = res
            return dp[amt]
        ret = helper(amount)
        return -1 if ret == m else ret
    

"""

    
    -------------- n = 11
   '
   '
   '
    sum(nCk) for k in range(12): 
    
    = 2^n = 2^11
    
    1,1,1,1,1,1,1,1,2
    
    
    {a,b,c} -> {},{a},{b},{b,c},{a,b},...,{a,b,c} # 8 
    
    {1,2,5} => 2^3 - - -
    sum (nCk) for k in range(4)


"""