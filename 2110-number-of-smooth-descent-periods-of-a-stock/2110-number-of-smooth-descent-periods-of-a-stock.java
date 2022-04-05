class Solution {
    public long getDescentPeriods(int[] prices) {
        int n = prices.length;
        int[] dp = new int[n];
        Arrays.fill(dp,1);
        long count = 1;
        for(int i = 1; i < n; i++){
            if(prices[i-1] - prices[i] == 1){
                dp[i] = dp[i-1] + 1;
            }
            count+= dp[i];
        }
        
        return count;
        
    }
}

