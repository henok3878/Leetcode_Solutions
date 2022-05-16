class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1:
            return -1
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
        n = len(grid)
        
        def is_inbound(i,j):
            return 0 <= i < n and 0 <= j < n
        
        queue = deque()
        queue.append((0,0,1))
        grid[0][0] = 1
        
        while(len(queue) > 0):
            
            curr = queue.popleft()
            if curr[0] == n- 1 and curr[1] == n- 1:
                return curr[2]
            for dirc in dirs:
                x = curr[0] + dirc[0]
                y = curr[1] + dirc[1]
                if(is_inbound(x,y) and grid[x][y] == 0):
                    queue.append((x,y,curr[2] + 1))
                    grid[x][y] = 1
            
        return -1
            