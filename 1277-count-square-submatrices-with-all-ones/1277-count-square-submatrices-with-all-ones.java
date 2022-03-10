class Solution {
    public int countSquares(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int total = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(matrix[i][j] == 0) continue;
                int l = (j - 1 < 0) ? 0 : matrix[i][j-1];
                int t = (i - 1 < 0 )? 0 : matrix[i-1][j];
                int d = (i - 1 < 0 || j - 1 < 0 ) ? 0 : matrix[i-1][j-1];
                
                int min = Math.min(l,t); min = Math.min(min,d);
                matrix[i][j] = min + 1;
                total += matrix[i][j];
                
            }
        }
        
        return total;
    }
}