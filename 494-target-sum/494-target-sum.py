class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        @lru_cache(None)
        def rec(i,curr):
            if(i  >= n):
                return 1 if curr == target else 0
            
            select = rec(i+1,curr - nums[i])
            skip = rec(i+1,curr + nums[i])
            
            return select + skip;
        
        
        return rec(0,0)