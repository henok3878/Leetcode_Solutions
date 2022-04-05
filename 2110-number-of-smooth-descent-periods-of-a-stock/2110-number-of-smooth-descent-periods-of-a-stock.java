class Solution {
    public long getDescentPeriods(int[] prices) {
        int n = prices.length;
        long count = 1, dp = 1;
        
        for(int i = 1; i < n; i++){
            
            dp = (prices[i-1] - prices[i] == 1) ? dp + 1 : 1;
            count += dp;
        }
        
        return count;
        
    }
}

