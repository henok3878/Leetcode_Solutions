class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        mod = 10 ** 9 + 7 
        visited = set() 
        
        dirs = [(0,-1),(1,0),(0,1),(-1,0)]
        
        def in_bound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        @cache 
        def helper(i,j):
            curr_path = 0
            for del_x, del_y in dirs:
                nxt_i,nxt_j = i + del_x, j + del_y 
                if in_bound(nxt_i,nxt_j) and grid[i][j] < grid[nxt_i][nxt_j]:
                    curr_path += helper(nxt_i,nxt_j) + 1
                    curr_path %= mod 
            ans[i][j] = curr_path 
            return curr_path 
        
        n = len(grid)
        m = len(grid[0])
        
        ans = [[1] * m for _ in range(n)]
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                helper(i,j)
                
        for i in range(n):
            for j in range(m):
                res += ans[i][j]
                res %= mod 
        return res + ( n * m) % mod 