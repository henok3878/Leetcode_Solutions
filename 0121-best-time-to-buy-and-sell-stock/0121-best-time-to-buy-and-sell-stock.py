class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn_sofar = prices[0] 
        mx_profit = 0
        for i in range(1,len(prices)):
            mx_profit = max(mx_profit, prices[i] - mn_sofar)
            mn_sofar = min(prices[i], mn_sofar)
        return mx_profit 
            