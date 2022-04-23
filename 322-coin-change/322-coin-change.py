class Solution:
    max = 10**6
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [self.max] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i-coin] + 1,dp[i])
        
        return -1 if dp[amount] == self.max else dp[amount]