class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(n+1)]

        for day in range(n-1, -1, -1):
            for have_stock in range(2):
                for sold_yesterday in range(2):
                    # Option 1: Do nothing
                    do_nothing = dp[day+1][have_stock][0]
                    
                    # Option 2: Trade (either buy or sell)
                    trade_outcome = 0
                    if have_stock:
                        trade_outcome = dp[day+1][0][1] + prices[day] # sell
                    elif not sold_yesterday:
                        trade_outcome = dp[day+1][1][0] - prices[day] # buy

                    dp[day][have_stock][sold_yesterday] = max(do_nothing, trade_outcome)
        
        return dp[0][0][0]





"""

0 -------> n
   <-------        

- Nothing (no trade): we don't condition 

- I wasn't allowed trading because of the cooldown: did we sell it yesterday? 
- I can buy if i don't have stock already: Do you have a stock? 
- I can sell if I have a stock already : Do you have stock already? 

1. I have stock
2. I don't have a sotck and sold it ont this day 

0: have no stock and sold it before yesterday 
1; have no stock and solde it yesterday 
2: have stock 

(day, state): # state = n, day = n 
    -> do nothing 
    -> either buy or sell 

day * state = N**2 

Normal recurssive: 2**(N**2)
with Cache: N**2 
"""