class Solution {
    int ans = 0;
    public int findTargetSumWays(int[] nums, int target) {
        helper(nums,target,0,0);
        return ans;
    }
    
    private void helper(int[] nums, int target,int sum, int idx){
        if(idx == nums.length){
            ans += (target == sum) ? 1 : 0;
            return;
        }
        
        helper(nums,target, sum + nums[idx], idx + 1);
        helper(nums,target,sum - nums[idx], idx + 1);
    }
}

/*
    [1,1,1,1,1], target = 3;
    
    


*/