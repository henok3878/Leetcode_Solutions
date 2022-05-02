class Solution:
    
   
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        m = 10**6
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = 0
        
        def helper(i,amt):
            if(i >= n or  amt < 0):
                return m 
            if(dp[i][amt] != -1):
                return dp[i][amt]
            
            select = helper(i,amt - coins[i]) + 1
            skip = helper(i+1,amt)
            
            dp[i][amt] = min(skip,select)
            return dp[i][amt]
        # print(dp)
        ret = helper(0,amount)
        return -1 if ret == m else ret