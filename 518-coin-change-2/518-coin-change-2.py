class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.dp = [0] * (amount + 1)
        self.dp[0] = 1
        
        for coin in coins: 
            for amt in range(coin,amount + 1):
                self.dp[amt] += self.dp[amt - coin]
                
        return self.dp[amount]
        