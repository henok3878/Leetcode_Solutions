class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = deque()
        n = len(grid) 
        m = len(grid[0]) 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j))
        level = 0
        while queue:
            size = len(queue) # size of current level 'level'
            for _ in range(size):
                x,y = queue.popleft() 
                for dx, dy in dirs:
                    new_x, new_y = x + dx, y + dy 
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == 1:
                        queue.append((new_x, new_y))
                        grid[new_x][new_y] = 2
                
            level += 1 
        poss = True 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    poss = False 
                    break 
            if not poss:
                break 
        if not poss:
            return -1
        return max(level - 1, 0)

        

                