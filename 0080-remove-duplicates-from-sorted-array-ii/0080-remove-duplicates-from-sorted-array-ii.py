class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0 
        ptr2 = 0 
        is_curr_double = False 
        n = len(nums)
        while (ptr2 < n):
            if(nums[ptr1] == nums[ptr2]):
                # todo
                if(ptr2 != ptr1 and (not is_curr_double)):
                    ptr1 += 1 
                    nums[ptr1] = nums[ptr2]
                    is_curr_double = True 
                ptr2 += 1 
            else:
                ptr1 += 1 
                nums[ptr1] = nums[ptr2]
                is_curr_double = False 
                ptr2 += 1 
        return ptr1 + 1