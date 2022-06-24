class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) 
        def transpose():
            for j in range(n):
                for i in range(j):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    
        def reflect():
            for i in range(n):
                matrix[i].reverse()
        
        transpose()
        reflect()