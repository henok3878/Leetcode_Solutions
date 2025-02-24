class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_valid = 1
        curr_i = 2 
        while curr_i < len(nums): 
            if nums[curr_i] != nums[last_valid-1]:
                nums[last_valid + 1] = nums[curr_i] 
                last_valid += 1 
            curr_i += 1 
        return last_valid + 1 