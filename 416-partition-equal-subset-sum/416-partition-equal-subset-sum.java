class Solution {
    public boolean canPartition(int[] nums) {
        int sum = Arrays.stream(nums).sum();
        if(sum%2 != 0) return false;
        int halfSum = sum / 2;
        
        Boolean[][] dp = new Boolean[nums.length][halfSum + 1];
        
        return helper(nums,0,halfSum,dp);
        
        
    }
    
    private boolean helper(int[] nums, int idx,int sum, Boolean[][] dp){
        if(sum == 0) return true; 
        else if(idx >= nums.length || sum < 0) return false;
        else if(dp[idx][sum] != null) return dp[idx][sum];
        
        return dp[idx][sum] =   helper(nums,idx + 1, sum - nums[idx],dp) ||
        helper(nums, idx + 1, sum, dp);
        
    }
}