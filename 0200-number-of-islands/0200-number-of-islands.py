class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0]) 
        
        def dfs(i,j):
            grid[i][j] = '0' # mark visited 
            for dx,dy in [(0,1), (1,0),(0,-1),(-1,0)]:
                x,y = i + dx, j + dy 
                if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                    dfs(x,y) 

        cnt = 0 
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == '1'):
                    dfs(i,j)
                    cnt += 1 
        
        return cnt 

        