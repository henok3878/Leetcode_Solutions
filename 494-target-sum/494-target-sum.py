class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if(abs(target) > total):
            return 0
        n = len(nums)
        dp = [0]*(2*total + 1)
        dp[total] = 1
        for i in range(n):
            temp_dp = [0] * (2*total + 1)
            
            for t in range(-1*total,total + 1, 1):
                prev = dp[total + t-nums[i]] if t - nums[i] >= -1*total else 0
                nxt = dp[total + t + nums[i]] if t + nums[i] <= total else 0
                
                temp_dp[total + t] = prev  + nxt
            dp = temp_dp
        return dp[total + target]