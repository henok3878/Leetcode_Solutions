class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) 
        MAX = 5000
        for i in range(n):
            for j in range(n):
                x,y = i,j 
                while matrix[x][y] > -1001 and 0 <= x < n and 0 <= y < n:
                    matrix[x][y], matrix[y][n-1-x]  = matrix[y][n-1-x],matrix[x][y] - MAX
                    x,y = y, n - 1 - x 
                    
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < -1001:
                    matrix[i][j] += MAX