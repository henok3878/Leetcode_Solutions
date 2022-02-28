class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> ans = new ArrayList<>();
        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            while(i + 1< nums.length && nums[i] + 1 == nums[i + 1]) i++;
            if(nums[i] == num){
                ans.add(num+"");
            }else ans.add(num+"->"+nums[i]);
            
        }
        return ans;
    }
}