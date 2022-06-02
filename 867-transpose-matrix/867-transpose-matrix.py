class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R = len(matrix)
        C = len(matrix[0])
        
        transpose = [[0 for i in range(R)]for _ in range(C)]
        for r in range(R):
            for c in range(C):
                transpose[c][r] = matrix[r][c]
        return transpose