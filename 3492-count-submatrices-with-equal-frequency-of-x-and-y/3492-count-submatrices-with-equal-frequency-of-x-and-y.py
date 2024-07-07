class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        prefixx = [[0] * (cols + 1) for _ in range(rows + 1)]
        prefixy = [[0] * (cols + 1) for _ in range(rows + 1)]
        cnt = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefixx[i][j] = prefixx[i - 1][j] + prefixx[i][j - 1] - prefixx[i-1][j -1] + int(grid[i-1][j-1] == 'X')
                prefixy[i][j] = prefixy[i - 1][j] + prefixy[i][j - 1] - prefixy[i-1][j -1] + int(grid[i-1][j-1] == 'Y')
                if(prefixx[i][j] == prefixy[i][j] and prefixx[i][j] > 0):
                    cnt += 1 
        return cnt 