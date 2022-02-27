class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] ans = new int[nums.length];
        int pivots = 0;
        int idx = 0;
        for(int num : nums){
            if(num == pivot) pivots++;
            else if(num < pivot) ans[idx++] = num;
        }
        while(pivots > 0){
            ans[idx++] = pivot;
            pivots--;
        }
        for(int num : nums){
            if(num > pivot) ans[idx++] = num;
        }
        return ans;
    }
}