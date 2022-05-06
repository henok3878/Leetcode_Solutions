class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        MAX = 10**6
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        dp[0][0] = 0
        
        def helper(i,amt):
            if i == n:
                return 0 if amt == 0 else MAX
            elif amt < 0:
                return MAX
            elif dp[i][amt] == -1:
                dp[i][amt] = min(1 + helper(i,amt - coins[i]), helper(i+1,amt))   
                
            return dp[i][amt]
        
        ans = helper(0,amount)
        
        return -1 if ans >= MAX else ans
    
    
        """
        - with out caching : 2^n
        - with caching: n * amount 
        So, we have avoided not to recompute 2^n - (n*amount) subproblems 
        """