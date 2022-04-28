class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def in_bound(x,y):
            return 0 <= x < n and 0 <= y < m
        
        def dfs(i,j,eff):
            if(i == n - 1 and j == m-1):
                return True
            
            visited[i][j] = True
            for dir in dirs:
                x , y = i + dir[0], j + dir[1]
                if(in_bound(x,y) and not visited[x][y] and abs(heights[i][j] -heights[x][y]) <= eff):
                    if(dfs(x,y,eff)):
                        return True
            return False
            
        
        n,m = len(heights), len(heights[0])
        
        left,right = 0, 10**6
        
        while(left < right):
            mid = (left + right) // 2
            visited = [[False for _ in range(m)]for _ in range(n)]
            if(dfs(0,0,mid)):
                right = mid
            else:
                left = mid + 1
        
        
        return left