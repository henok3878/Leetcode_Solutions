class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        n = len(grid) 
        m = len(grid[0]) 

        dirs = [(0,1), (1, 0), (0,-1), (-1,0)]
        empty = 2
        st_x = st_y = end_x = end_y = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    empty += 1 
                elif grid[i][j] == 2:
                    end_x = i 
                    end_y = j 
                elif grid[i][j] == 1:
                    st_x = i 
                    st_y = j
        
        seen = [[False] * m for _ in range(n)]
        def dfs(x, y,path_len):
            if(x == end_x and y == end_y):
                return int(path_len == empty) 
            seen[x][y] = True 
            res = 0
            for dx,dy in dirs:
                new_x = x + dx 
                new_y = y + dy 
                if (0 <= new_x < n and 0 <= new_y < m and (grid[new_x][new_y] != -1) and not seen[new_x][new_y]):
                    res += dfs(new_x, new_y,path_len + 1) 
            seen[x][y] = False 
            return res 
        
        # print(empty)
        return dfs(st_x, st_y, 1)
        


