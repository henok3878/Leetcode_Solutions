class Solution:
    max = 10**6
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [self.max]*(amount + 1)
        dp[0] = 0
        for n in range(amount + 1):
            for coin in coins:
                if n >= coin:
                    dp[n] = min(dp[n-coin] + 1, dp[n])
                    
        return -1 if dp[amount] == self.max else dp[amount] 