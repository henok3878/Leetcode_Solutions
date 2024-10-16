class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None) 
        def helper(i, amt):
            if amt == amount:
                return 0 
            elif amt > amount or i >= len(coins):
                return float('inf') 
            # choose
            op1 = helper(i, amt + coins[i]) + 1
            # skip 
            op2 = helper(i + 1, amt) 

            return min(op1, op2) 

        res = helper(0, 0) 
        if res == float('inf'):
            return -1 
        return res
            
    

'''
We could try to check all the possible subsets with sum <= amount.

(i, amt_sofar): # i represents the curr coin we are considering, amt_sofar is amt made

(i, amt_sofar) -> 1) (i, amt_sofar + coin[i]) # use ith coin 
                  2) (i + 1, amt_sofar) # skip this coin 

# the number of functions calls: 2 ** (amt * n)

# unique number of function calls: amt * n 

# If we use memoization, we can save: (2**(amt * n)) - (amt * n) number of function calls. 


'''