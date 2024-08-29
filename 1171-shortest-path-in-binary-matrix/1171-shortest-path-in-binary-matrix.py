class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1 
        n = len(grid) 

        step = 0 
        q = deque() 
        q.append((0,0))
        grid[0][0] = 1 
        dirs = [(1,0),(1,1), (1, -1),(-1,0),(-1,1),(-1,-1), (0,1), (0,-1)]

        while q:
            s = len(q) 
            for _ in range(s):
                x,y = q.popleft() 
                if x == n - 1 and y == n -1:
                    return step + 1
                for dx,dy in dirs:
                    xx,yy = x + dx, y + dy 
                    if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 0:
                        q.append((xx,yy)) 
                        grid[xx][yy] = 1 
            step += 1 
        return -1
