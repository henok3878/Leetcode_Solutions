class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        total = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    adj_min = min(matrix[i-1][j-1],matrix[i-1][j], matrix[i][j-1]) if i -1 >= 0 and j - 1 >= 0 else 0
                    matrix[i][j] = adj_min + 1
        for i in range(m):
            for j in range(n):
                    total += matrix[i][j]
        #print(matrix)
        return total
    
    
"""

[0, 1, 1, 1]
[1, 1, 2, 2]
[0, 1, 2, 3]]


"""