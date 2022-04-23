class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        ans = -1
        for i in range(N):
            for j in range(0,i):
                if(nums[i] > nums[j]):
                    dp[i] = max(dp[j] + 1,dp[i])
            ans = max(dp[i],ans)
                
        return ans
        