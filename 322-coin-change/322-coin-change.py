class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        MAX = 10**6
        @lru_cache(None)
        def helper(amt):
            if(amt == 0):
                return 0
            elif amt < 0:
                return MAX 
            res = MAX
            for c in coins:
                res = min(res,helper(amt - c) + 1)
            
            return res
        
        ans = helper(amount)
        
        return -1 if ans == MAX else ans