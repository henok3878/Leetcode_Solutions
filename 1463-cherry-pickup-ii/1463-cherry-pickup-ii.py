class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def in_bound(i,j):
            return 0 <= i <= n and 0 <= j < m 
        
        moves = [-1,0,1]
        
        dp = [[ [float('-inf') for col in range(m)] for col in range(m)] for row in range(n + 1)]
        
        for i in range(m):
            for j in range(m):
                dp[n][i][j] = 0
        
        for i in range(n-1,-1,-1):
            for j1 in range(m-1,-1,-1):
                for j2 in range(0,m):
                    #choose 
                    score1 = grid[i][j1]
                    grid[i][j1] = 0 
                    score2 = grid[i][j2]
                    grid[i][j2] = 0
                    score = score1 + score2 
                    #Explore 
                    for m1 in moves:
                        for m2 in moves:
                            if in_bound(i + 1, j1 + m1) and in_bound(i + 1, j2 + m2):
                                dp[i][j1][j2] = max(dp[i][j1][j2], dp[i + 1][j1 + m1][j2 + m2] + score)
                    #unchoose 
                    grid[i][j2] = score2 
                    grid[i][j1] = score1 
        
        return dp[0][0][m-1]
 
                    
            