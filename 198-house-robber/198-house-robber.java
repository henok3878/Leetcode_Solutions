class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n < 2 )return nums[0];
        int[] dp = new int[n];
        dp[0] = nums[0]; dp[1] = nums[1]; 
        for(int i = 2; i < n;i++){
            int i2 = (i-2 < 0) ? Integer.MIN_VALUE : dp[i-2];
            int i3 = (i - 3 < 0) ? Integer.MIN_VALUE : dp[i-3];
            dp[i] = Math.max(i2, i3) + nums[i];
        }
        return Math.max(dp[n-2],dp[n-1]);
    }
}