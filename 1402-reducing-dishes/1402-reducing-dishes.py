class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort() 
        n = len(satisfaction)
        dp = [[0] * (n + 2) for _ in range(n + 1)]
        for i in range(n -1,-1,-1):
            for j in range(n,0,-1):
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1] + satisfaction[i] * j)
        
        return dp[0][1]
    """
    skip = helper(i + 1, time)
            select = helper(i + 1, time + 1) + (satisfaction[i] * time) 
    """