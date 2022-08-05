class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache 
        def helper(target):
            if target == 0:
                return 1
            elif target < 0:
                return 0
            res = 0 
            for num in nums:
                res += helper(target - num)
            return res
        
        return helper(target)
            