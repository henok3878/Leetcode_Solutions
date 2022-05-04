class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if(total % 2 != 0):
            return False
        target = total // 2
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(1,n + 1):
            for t in range(target + 1):
                res = dp[i-1][t - nums[i-1]] if t - nums[i-1] >= 0 else False
                dp[i][t] = dp[i-1][t] or res
        # print(dp)
        return dp[n][target]