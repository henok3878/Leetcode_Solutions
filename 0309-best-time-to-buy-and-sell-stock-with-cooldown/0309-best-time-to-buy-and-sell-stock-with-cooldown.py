class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache 
        def helper(day,have_stock,sold_yesterday):
            if day == n:
                return 0
            do_nothing = helper(day + 1, have_stock, False) 
            trade_outcome = 0
            if have_stock:
                trade_outcome = helper(day + 1, False, True) + prices[day] # sell 
            elif not sold_yesterday:
                trade_outcome = helper(day + 1, True, False) - prices[day] # buy 
            
            return max(do_nothing,trade_outcome) 

        return helper(0,False, False)

   
                




        


"""

0 -------> n
   <-------        

- Nothing (no trade): we don't condition 

- I wasn't allowed trading because of the cooldown: did we sell it yesterday? 
- I can buy if i don't have stock already: Do you have a stock? 
- I can sell if I have a stock already : Do you have stock already? 

1. I have stock
2. I don't have a sotck and sold it ont this day 

X: as i don't a stock but sold it on the X'th day 
0: I have stock on my hand 

(day, state): # state = n, day = n 
    -> do nothing 
    -> either buy or sell 

day * state = N**2 

Normal recurssive: 2**(N**2)
with Cache: N**2 
"""