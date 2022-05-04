class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if(total % 2 != 0):
            return False
        target = total // 2
        n = len(nums)
        dp = [False] * (target + 1)
        dp[0] = True
        
        for i in range(n):
            for t in range(target,nums[i]-1,-1):
                dp[t] = dp[t-nums[i]] or dp[t]
        # print(dp)
        return dp[target]