class Solution {
    public int maxNonOverlapping(int[] nums, int target) {
        int n = nums.length;
        int res = 0;
        Map<Integer,Integer> dp = new HashMap<>();
        dp.put(0,0);
        int sum = 0;
        
        for(int i = 0; i < n;i++){
            sum += nums[i];
            
            if(dp.containsKey(sum - target)){
                res = Math.max(res,dp.get(sum-target) + 1);
            }
            dp.put(sum,res);
        }
        
        return res;
    }
}

/*

*/
