class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        
        n,m = len(grid), len(grid[0])
        
        if(grid[0][0] == ')' or grid[n-1][m-1] == '('):
            return False
        
        def is_valid(i,j):
            return 0 <= i < n and 0 <= j < m
        @cache
        def dfs(i,j,cnt):
            if i == n -1 and j == m - 1:
                return True if cnt == 1 else False
            
            if cnt == 0:
                if grid[i][j] == ')':
                    return False
                else:
                    cnt += 1
            else:
                if grid[i][j] == ')':
                    cnt -= 1
                else:
                    cnt += 1
    
            res = is_valid(i,j+1) and dfs(i,j+1,cnt)
            res = res or (is_valid(i+1,j) and dfs(i+1,j,cnt))
            
            return res
        
        return dfs(0,0,0)