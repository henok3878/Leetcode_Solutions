class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N = len(coins)
        dp = [[0]*(amount+1) for _ in range(N + 1)]
        dp[0][0] = 1
        
        for amt in range(amount + 1):
            for i in range(1, N + 1):
                dp[i][amt] = dp[i-1][amt]
                if amt - coins[i-1] >= 0:
                    dp[i][amt] += dp[i][amt - coins[i-1]]
            
        return dp[N][amount]