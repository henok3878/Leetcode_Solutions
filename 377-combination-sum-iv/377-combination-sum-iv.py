class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] * (target + 1) 
        dp[0] = 1 
        
        for i in range(1,target + 1):
            for num in nums:
                prev_st = dp[i - num] if i - num >= 0 else 0 
                dp[i] += prev_st 
        
        #print(dp)
        return dp[target]
        
        