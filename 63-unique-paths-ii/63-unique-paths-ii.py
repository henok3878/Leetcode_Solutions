class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dp = [[None for _ in range(m)] for _ in range(n)]
        
        def dfs(i,j):
            if i == n - 1 and j == m - 1:
                return 1
            if dp[i][j] != None:
                return dp[i][j]
            down = 0
            if(0 <= i + 1 < n and obstacleGrid[i][j] != 1):
                down = dfs(i + 1, j)
            
            right = 0
            if(0 <= j + 1 < m and obstacleGrid[i][j] != 1):
                right = dfs(i, j + 1)
            
            dp[i][j] = down + right
            
            return dp[i][j]
         
        if(obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1] == 1):
            return 0
        return dfs(0,0)