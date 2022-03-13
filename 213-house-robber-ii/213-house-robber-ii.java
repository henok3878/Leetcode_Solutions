class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 1) return nums[0];
        else if(n== 2) return Math.max(nums[0],nums[1]);
        
        int[] dp = new int[n];
        dp[0] = nums[0];
        int max = nums[0];
        for(int i = 1; i < n - 1; i++){
            int prev = (i - 2 < 0) ? 0 : dp[i-2];
            int prev2 = (i - 3 < 0) ? 0 : dp[i-3];
            dp[i] = nums[i] + Math.max(prev,prev2);
            max = Math.max(max,dp[i]);
        }
        
        dp[1] = nums[1]; dp[0] = 0;
        for(int i = 2; i < n; i++){
            int prev = (i - 2 < 0) ? 0 : dp[i-2];
            int prev2 = (i - 3 < 0) ? 0 : dp[i-3];
            dp[i] = Math.max(prev,prev2) + nums[i];
            max = Math.max(max,dp[i]);
        }
        
        
        return max;
        
    }
}