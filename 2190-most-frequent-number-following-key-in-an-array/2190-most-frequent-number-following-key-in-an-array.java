class Solution {
    public int mostFrequent(int[] nums, int key) {
        Map<Integer,Integer> counts = new HashMap<>();
        int max = 0;
        int ans = -1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i-1] == key){
                int p = counts.getOrDefault(nums[i],0) + 1;
                counts.put(nums[i],p);
                if(p > max){
                    max = p;
                    ans = nums[i];
                }
            }
        }

        return ans;
    }
}