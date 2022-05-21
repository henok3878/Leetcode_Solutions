class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        MAX = 10**20
        
        @cache
        def dfs(i,curr):
            if(curr > amount):
                return MAX
            if i == len(coins):
                return 0 if amount == curr else MAX
            
            select = MAX
            if(amount - coins[i] >= 0):
                select = 1  + dfs(i, curr + coins[i])
            skip = dfs(i + 1, curr)
            
            return min(select,skip)
        
        ans = dfs(0,0)
        return ans if ans != MAX else -1
        
        
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