class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_valid = 0 
        curr_i = 1 
        twice = False
        while curr_i < len(nums): 
            if nums[curr_i] != nums[last_valid] or not twice:
                nums[last_valid + 1] = nums[curr_i] 
                if(nums[curr_i] == nums[last_valid]):
                    twice = True
                else:
                    twice = False 
                last_valid += 1 
            curr_i += 1 
        return last_valid + 1 