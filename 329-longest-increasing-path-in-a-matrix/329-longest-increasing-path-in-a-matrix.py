class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        dp = [[None for _ in range(m)] for _ in range(n)]
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(i,j):
            #print(i,j)
            #print("f", dp)
            if dp[i][j] != None:
                return dp[i][j]
                
            res = 1
            for adj in dirs:
                x,y = adj[0] + i, adj[1] + j
                if 0 <= x < n and 0 <= y < m and matrix[i][j] < matrix[x][y]:
                    res = max(res,1 + dfs(x,y))
            dp[i][j] = res
            #print("l",dp)
            return res
        
        ans = 0
        
        for i in range(n):
            for j in range(m):
                ans = max(ans,dfs(i,j))
        return ans