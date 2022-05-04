class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if(total % 2 != 0):
            return False
        half = total // 2
        
        @lru_cache(None)
        def helper(i,curr):
            if curr < 0:
                return False
            elif curr == 0:
                return True
            
            res = False
            for nxt in range(i,n):
                res = res or helper(nxt + 1, curr - nums[nxt])
                
            return res
        
        return helper(0,half)