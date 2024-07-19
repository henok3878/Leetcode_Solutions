class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        min_row = [[False] * C for _ in range(R)] 
        for i in range(R):
            mn = 0
            for j in range(C):
                if(matrix[i][j] < matrix[i][mn]):
                    mn = j 
            min_row[i][mn] = True 

        ans = []
        for j in range(C):
            mx = 0 
            for i in range(R):
                if(matrix[i][j] > matrix[mx][j]):
                    mx = i 
            if min_row[mx][j]:
                ans.append(matrix[mx][j])
        
        return ans 
