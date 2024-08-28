class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(grid) 
        m = len(grid[0]) 

        def is_boarder(i,j):
            return (i == 0 or j == 0 or j == m-1 or i == n -1)

        def dfs(i,j):
            grid[i][j] = '#' 
            for dx,dy in [(1,0), (0,1),(-1,0),(0,-1)]:
                x,y = i + dx, j + dy 
                if (0 <= x < n and 0 <= y < m) and grid[x][y] == 'O':
                    dfs(x,y) 

        for i in range(n):
            for j in range(m):
                if is_boarder(i,j) and grid[i][j] == 'O':
                    dfs(i,j)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '#':
                    grid[i][j] = 'O'
                elif grid[i][j] == 'O':
                    grid[i][j] = 'X'
    
            
        