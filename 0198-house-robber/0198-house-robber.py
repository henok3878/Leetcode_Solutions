class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) 
        dp = [0] * 3 
        for num in nums:
            dp[2] = max(dp[0] + num, dp[1]) 
            dp[0],dp[1] = dp[1], dp[2]
        return dp[-1]
        