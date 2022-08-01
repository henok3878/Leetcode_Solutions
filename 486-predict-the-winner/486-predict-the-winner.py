class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        n = len(nums)
        dp = [[0] * n  for _ in range(n)] 
        for l in range(n-1,-1,-1): 
            for r in range(n):
                if l > r: 
                    dp[l][r] = 0 
                else:
                    left = dp[l+1][r] if l + 1 < n else 0 
                    right = dp[l][r-1] if r - 1 >= 0 else 0 
                    dp[l][r] = max(nums[l] - left, nums[r] - right)
                    
        return dp[0][n-1] >= 0