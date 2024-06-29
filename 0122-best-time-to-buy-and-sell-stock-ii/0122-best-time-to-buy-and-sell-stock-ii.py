class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0 
        buy = float('inf')
        for sell in prices:
            if(sell > buy):
                ans += (sell - buy)
                buy = sell 
            else:
                buy = sell 
        return ans 
