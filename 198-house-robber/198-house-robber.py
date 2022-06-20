class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def helper(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0],nums[1])
            
            return max(helper(i-1),helper(i-2) + nums[i])
        
        return helper(n-1)
            