class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if(n < 2 )return nums[0];
        
        int[] dp = new int[n];
        int max = nums[0];
        dp[0] = nums[0];
        for(int i = 1; i < n;i++){
            dp[i] = nums[i];
            for(int j = 0; j < i - 1;j++)
                dp[i] = Math.max(dp[i], nums[i] + dp[j]);
            max = Math.max(dp[i], max);
        }
        return max;
    }
}