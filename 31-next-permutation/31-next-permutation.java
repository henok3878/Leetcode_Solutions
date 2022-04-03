class Solution {
    public void nextPermutation(int[] nums) {
        
        int n = nums.length;
        int idx = -1;
        
        for(int i = n-1; i > 0; i--){ 
            if(nums[i-1] < nums[i]){
                idx = i-1;
                break;
            }
        }
        if(idx != -1){
            int minIdx = -1;
            int min = Integer.MAX_VALUE;

            for(int j = idx + 1; j < n;j++){
                if(nums[j] > nums[idx] && min >= nums[j]){
                    minIdx = j;
                    min = nums[j];
                }
            }
            if(idx != -1 && minIdx != -1){
                swap(nums,idx,minIdx);
            } 
        }
        reverse(nums,idx+1);   
    }
    
    private void reverse(int[] nums, int idx){
        int n = nums.length;
        int left = idx, right = n-1;
        while(left <= right){
            swap(nums,left,right);
            left++;
            right--;
        }
    }
    
    private void swap(int[] nums, int i, int j){
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }
}

/*

[2,3,1,3,3]

[1,2,3] => 123 132 213 231 312 321 123 (cycle)

1234 => 1243 => 1324 => 1342 => 1423 => 1432 => 2134 => 2

115 => 

*/