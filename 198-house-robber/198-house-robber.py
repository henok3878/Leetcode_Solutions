class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def rec(i):
            if i < 0:
                return 0
            if(dp[i] != -1):
                return dp[i]
            
            skip = rec(i-1)
            select = nums[i] + rec(i-2)
            
            dp[i] = max(skip,select)
            
            return dp[i]
        
        return rec(n-1)
                
                