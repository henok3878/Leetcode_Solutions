class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        temp = [[0 for _ in range(n)] for _ in range(m)] 
        for i in range(m):
            for j in range(n):
                temp[i][j] = grid[i][j] 
                
        for i in range(m-2,-1,-1):
            for j in range(n):
                if grid[i][j] == 0:
                    continue 
                #left 
                left = grid[i + 1][j - 1] if j > 0 else 0 
                #bottom 
                bottom = grid[i + 1][j] 
                #right 
                right = grid[i + 1][j + 1] if j + 1 < n else 0 
                
                grid[i][j] = 1 + min(left,bottom,right) 
        for i in range(1,m):
            for j in range(n):
                if temp[i][j] == 0:
                    continue 
                #left 
                left = temp[i - 1][j - 1] if j > 0 else 0 
                #up 
                bottom = temp[i - 1][j] 
                #right 
                right = temp[i - 1][j + 1] if j + 1 < n else 0 
                
                temp[i][j] = 1 + min(left,bottom,right) 
        
        ans = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans += grid[i][j] - 1 
                if temp[i][j] != 0:
                    ans += temp[i][j] - 1 
        
        return ans 