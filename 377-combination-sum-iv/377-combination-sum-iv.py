class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache 
        def helper(idx,target):
            if target == 0:
                return 1
            elif target < 0 or idx >= len(nums):
                return 0
            res = 0 
            for i in range(len(nums)):
                res += helper(i,target - nums[i])
            return res
        
        return helper(0,target)
            