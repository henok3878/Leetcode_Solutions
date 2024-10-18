class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)
        no_stock = [0] * n
        have_stock = [float('-inf')] * n 
        have_stock[0] = -prices[0]
        for i in range(1,n):
            have_stock[i] = max(have_stock[i - 1], no_stock[i-1] - prices[i]) 
            no_stock[i] = max(no_stock[i - 1], have_stock[i - 1] + prices[i] - fee) 
        
        return max(no_stock[-1], have_stock[-1])


"""
For each day we can choose:
- to Sell if we have stock already 
- to Buy if we don't have a stock 
- to do nothing 


have, don't have
"""