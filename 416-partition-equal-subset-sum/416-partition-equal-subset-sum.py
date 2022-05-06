class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if(total % 2 != 0):
            return False
        half = total // 2
        
        @lru_cache(None)
        def helper(i,curr):
            if curr < 0 or i >= n:
                return False
            elif curr == 0:
                return True
            
            return helper(i + 1, curr - nums[i]) or helper(i+1,curr)
        
        return helper(0,half)