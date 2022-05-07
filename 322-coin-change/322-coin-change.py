class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = 10**6
        n = len(coins)
        
        @lru_cache(None)
        def helper(i,amt):
            if i >= n or amt < 0:
                return MAX
            if amt == 0:
                return 0
            res = MAX
            for nxt in range(i,n):
                res = min(res, 1 + helper(nxt,amt - coins[nxt]))
            
            return res
            
        ans = helper(0,amount)
        return -1 if ans >= MAX else ans 
        
        
        
        """
            
        
        The obvious answer: 
            -> Generate every combination
            -> Check if sum(combnination) == target 
            -> track the min length
            
            TIME COMPLEXITY: 2^max_len , assuming we keep track of the sum while generating
                -> max_len becuase we have infinte number of each kind of coin
                
               
               
              
              
        coins = [1,2,5], amount = 11
        
        if I used 1: 
            amount = 10, min ways to make 10 using:
                option1: using current and prev coins
                    -> in this case you process amt only using available coins so far 
                option2: using any possible coins you want 
                    -> in this case you have to compute amount sequentially 
                    
                    
                why both cases works:
                    -> option 1 works because it covers every combination that can be formed
                    -> option 2 works for the same reason but it also premituations of combinations. But if the problems was not optimization problem, this method will overcount combinations.
                    
                    amt called n times 
                    total call => amount+1 * n unique problems 
                    
                    total = n^(amount + 1)
            
        
        
        
        
        """