class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        mn = float('inf') 
        for price in prices:
            if(price - mn > 0):
                ans += price - mn 
                mn = price 
            mn = min(price, mn) 
        return ans 