class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if(total % 2 != 0):
            return False
        target = total // 2
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = True
        
        for t in range(target + 1):
            for i in range(1,n+1):
                prev = dp[i-1][t-nums[i-1]] if t - nums[i-1] >= 0 else False
                dp[i][t] = dp[i-1][t] or prev
        return dp[n][target]
        
        ''' 
        Another implementation: In this case, even though it makes sense to convert 2D -> 1D doing that will result in wrong answer. Becuase, we are asking defferent question for each subproblem. (which is 'Is it possible to make target, using the whole elements in the array?')
        for i in range(1,n + 1):
            for t in range(target + 1):
                res = dp[i-1][t - nums[i-1]] if t - nums[i-1] >= 0 else False
                dp[i][t] = dp[i-1][t] or res
        # print(dp)
        return dp[n][target]
        '''
        
        
        