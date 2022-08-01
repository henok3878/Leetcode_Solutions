class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [0] * n  
        for l in range(n-1,-1,-1): 
            for r in range(l,n):
                if l == r: 
                    dp[r] = nums[l] 
                else:
                    dp[r] = max(nums[l] - dp[r], nums[r] - dp[r-1])
                    
        return dp[n-1] >= 0