class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [0] * n  
        for l in range(n-1,-1,-1): 
            for r in range(n):
                if l > r: 
                    dp[r] = 0 
                else:
                    left = dp[r] if l + 1 < n else 0 
                    right = dp[r-1] if r - 1 >= 0 else 0 
                    dp[r] = max(nums[l] - left, nums[r] - right)
                    
        return dp[n-1] >= 0