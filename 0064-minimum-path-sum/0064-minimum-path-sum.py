class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def in_bound(x,y):
            return 0 <= x < n and 0 <= y < m 
        
        @cache 
        def helper(x, y):
            if not in_bound(x, y):
                return float('inf') # inf will invalidate this path 
            elif x == (n - 1) and y == (m - 1):
                return grid[x][y] 
            down = helper(x + 1, y) 
            right = helper(x, y + 1) 
            return min(down, right) + grid[x][y] 
        
        return helper(0, 0)
        

        
        

"""
1. is in bound checker function
2. a recurssive function that explores for each cell 
    - Base case: 
        - if the indices are out of bound then not valid 
        - if we reached to the required cell, we return its value 
    - Recurrence:
        ans(x,y) = max(ans(x + 1, y), ans(x, y + 1)) + val(x,y)
"""