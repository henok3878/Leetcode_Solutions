class Solution {
    public long maxAlternatingSum(int[] nums) {
        int n = nums.length;
        long evenMax = 0, oddMax = 0;
        for(int i = 0; i < n; i++){
            long odd = oddMax;
            oddMax = Math.max(oddMax,evenMax - nums[i]); 
            evenMax = Math.max(Math.max(nums[i],evenMax),odd + nums[i]);
        }
        
        return evenMax;
    }
}