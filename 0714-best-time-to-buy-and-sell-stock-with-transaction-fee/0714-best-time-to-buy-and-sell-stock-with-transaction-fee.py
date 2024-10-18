class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        @cache 
        def helper(day, have_stock):
            if day >= n:
                return 0
            if have_stock:
                # sell or do nothing 
                return max(helper(day + 1, False) + prices[day] - fee, helper(day + 1,True)) 
            else:
                # buy or do nothing 
                return max(helper(day + 1, True) - prices[day], helper(day + 1, False)) 
        return helper(0,False)
"""
I have to choices:
    1. Buy if i have no stock 
    2. Sell if I have stock 
    3. Skip (no trade)

    (day, have_stock = True/ False)

    have_stock == -1, we don't have any stock 
    if have stock > 0 we have stock 
"""