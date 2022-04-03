class Solution {
    public void nextPermutation(int[] nums) {
        
        int n = nums.length;
        
        boolean found = false;
        for(int i = n-1; i >= 0; i--){
            int minIdx = -1;
            int min = Integer.MAX_VALUE;
            
            for(int j = i; j < n; j++){
                if(nums[j] > nums[i] && min > nums[j]){
                    minIdx = j;
                    min = nums[j];
                    found = true;
                }
            }
            if(found){
                nums[minIdx]  = nums[i];
                nums[i] = min;
                Arrays.sort(nums,i+1,n);
                break;
            }
        }        
        if(!found) Arrays.sort(nums);
       
    }
}

/*

[1,2,3] => 123 132 213 231 312 321 123 (cycle)

1234 => 1243 => 1324 => 1342 => 1423 => 1432 => 2134 => 2

115 => 

*/