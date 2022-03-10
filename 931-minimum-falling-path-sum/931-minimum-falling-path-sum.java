class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        
        for(int i = 0; i < m; i++){
            for(int j = 0;j < n; j++){
                int ld = (i - 1 < 0 || j - 1 < 0) ? Integer.MAX_VALUE : matrix[i-1][j-1];
                int rd = (i - 1 < 0 || j + 1 >= n) ? Integer.MAX_VALUE : matrix[i-1][j+1];
                int t = (i-1 < 0) ? 0 : matrix[i-1][j];
        
                matrix[i][j] += Math.min(Math.min(ld, rd), t);
        
            }
        }
    
        
        int ans = Integer.MAX_VALUE;
        for(int num : matrix[m-1]) ans = Math.min(ans,num);
        
        return ans;
        
    }
}