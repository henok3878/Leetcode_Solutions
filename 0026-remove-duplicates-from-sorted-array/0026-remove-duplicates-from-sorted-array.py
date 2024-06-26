class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0 
        ptr2 = 0 
        n = len(nums)
        while(ptr2 < n):
            if(nums[ptr1] == nums[ptr2]):
                ptr2 += 1
            else:
                ptr1 += 1 
                nums[ptr1] = nums[ptr2] 
                
        return ptr1 + 1