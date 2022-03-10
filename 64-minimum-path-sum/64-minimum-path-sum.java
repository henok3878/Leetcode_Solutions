class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m+1][n+1];
        for(int[] row : dp) Arrays.fill(row,Integer.MAX_VALUE);
        dp[1][0] = 0;
        for(int i = 1; i <= m; i++){
            for(int j = 1;j <= n; j++){
                dp[i][j] = Math.min(dp[i][j-1], dp[i-1][j]) + grid[i-1][j-1];
            }
        }
        return dp[m][n];
    }
}