class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def helper(i,j,  n,  m):
            if(n == 0 or m == 0): return []

            layer = []
            # left to right 
            for jj in range(j, j + m):
                layer.append(matrix[i][jj])

            # top to bottom 
            for ii in range(i + 1, i + n -1):
                layer.append(matrix[ii][j + m - 1])
            if n > 1:
                # right to left 
                for jj in range(j + m-1,j-1,-1):
                    layer.append(matrix[i + n - 1][jj]) 
            if m > 1:
                # bottom to up 
                for ii in range( i + n - 2,i,-1):
                    layer.append(matrix[ii][j])
            
            new_n = (n - 2) if n > 1 else (n - 1)
            new_m = (m - 2) if m > 1 else (m - 1)
            
            # print("layer:", layer)
            return layer + helper(i + 1, j + 1, new_n, new_m)
        
        return helper(0,0, len(matrix), len(matrix[0]))
