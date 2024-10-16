class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache 
        def minCoins(amt):
            if amt == 0:
                return 0
            elif amt < 0:
                return float('inf') # we can't make 
            res = float('inf')
            for coin in coins:
                res = min(res, minCoins(amt - coin) + 1)
            return res 

        res = minCoins(amount) 
        if res == float('inf'):
            return -1
        return res