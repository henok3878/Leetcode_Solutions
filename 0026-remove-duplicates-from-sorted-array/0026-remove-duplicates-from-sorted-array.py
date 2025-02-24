class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_valid = 0 
        curr_i = 1
        n = len(nums) 
        while curr_i < n:
            if nums[curr_i] != nums[last_valid]:
                nums[last_valid + 1] = nums[curr_i] 
                last_valid += 1 
            curr_i += 1 
        return last_valid + 1 
