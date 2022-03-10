class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int buy = Integer.MAX_VALUE, profit = 0 ;
        
        for(int i = 0; i < n;i++){
            buy = Math.min(prices[i],buy);
            profit = Math.max(prices[i] - buy,profit);
        }
        
        return profit;
    }
}