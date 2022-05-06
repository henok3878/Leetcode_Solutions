class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        MAX = 10**6
        
        @lru_cache(None)
        
        def helper(i,amt):
            if i == n:
                return 0 if amt == 0 else MAX
            elif amt < 0:
                return MAX
            
            return  min(1 + helper(i,amt - coins[i]), helper(i+1,amt))             
        
        ans = helper(0,amount)
        
        return -1 if ans >= MAX else ans
    
    
    """
    [1,2,5], 11 
    
    select
    skip
    
    """