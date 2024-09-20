class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def helper(amt):
            if(amt == 0): return 0
            elif amt < 0: return float('inf') 
            res = float('inf')
            for c in coins:
                res = min(res, helper(amt - c) + 1)
            return res 
        ans = helper(amount) 
        return ans if ans != float('inf') else -1
