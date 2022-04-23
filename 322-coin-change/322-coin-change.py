class Solution:
    
    max = 10**6
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        dp = [[self.max for _ in range(amount + 1)] for _ in range(N + 1)]
        
        for i in range(N + 1):
            dp[i][0] = 0
        
        for i in range (1,N + 1):
            for n in range (1,amount + 1):
                coin = coins[i-1]
                dp[i][n] = dp[i-1][n]
                if n >= coin:
                    dp[i][n] = min(dp[i][n], dp[i][n-coin] + 1)
                                        
        return -1 if dp[N][amount] == self.max else dp[N][amount]
        
        