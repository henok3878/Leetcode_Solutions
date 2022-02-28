class Solution {
    public int search(int[] nums, int target) {
        int pivot = findPivot(nums);
        if(target < nums[0])
            return find(nums,target,pivot + 1, nums.length - 1);
        else 
            return find(nums,target,0,pivot);
        
    }
    
    private int find(int[] nums, int target, int st, int end){
        while(st <= end){
            int mid = st + (end - st) / 2;
            if(nums[mid] > target) end = mid - 1;
            else if(nums[mid] < target) st = mid + 1;
            else return mid;
        }
        return -1;
    
    }
    
    private int findPivot(int[] nums){
        int st = 0; int end = nums.length - 1;
        
        while(st <= end){
            int mid = st + (end - st)/2;
            if(mid + 1 < nums.length && nums[mid+1] < nums[mid]) return mid;
            else if(nums[mid] < nums[0]) end = mid - 1;
            else st = mid + 1;
        }
        
        return (st == nums.length) ? st - 1 : st;
    }
}