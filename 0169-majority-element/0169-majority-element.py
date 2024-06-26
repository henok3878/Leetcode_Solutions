class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() 
        i = 0 
        mx_cnt = 0 
        ans = 0 # the inital value doesn't matter 
        n = len(nums)
        while (i < n):
            j = i 
            while (j < n and nums[j] == nums[i]):
                j += 1 
            curr_cnt = (j - i)
            if(mx_cnt < curr_cnt):
                mx_cnt = curr_cnt 
                ans = nums[i]
            i = j
        return ans