class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        no_stock = 0
        have_stock = -prices[0]
        for i in range(1,n):
            prev_have_stock = have_stock 
            prev_no_stock = no_stock 
            have_stock = max(prev_have_stock, no_stock - prices[i]) 
            no_stock= max(prev_no_stock, have_stock + prices[i] - fee) 
        
        return max(no_stock, have_stock)


"""
For each day we can choose:
- to Sell if we have stock already 
- to Buy if we don't have a stock 
- to do nothing 


have, don't have
"""