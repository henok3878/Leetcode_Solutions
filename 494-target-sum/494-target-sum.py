class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if(abs(target) > total):
            return 0
        n = len(nums)
        dp = [[0 for _ in range(2*total + 1)] for _ in range(n+1)]
        dp[0][total] = 1
        
        for i in range(n):
            for t in range(-1*total,total + 1, 1):
                prev = dp[i][total + t-nums[i]] if t - nums[i] >= -1*total else 0
                nxt = dp[i][total + t + nums[i]] if t + nums[i] <= total else 0
                
                dp[i+1][total + t] = prev  + nxt
                
        return dp[n][total + target]