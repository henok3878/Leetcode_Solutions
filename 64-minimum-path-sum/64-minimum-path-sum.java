class Solution {
    public int minPathSum(int[][] grid) {
        int[][] dp = new int[grid.length][grid[0].length];
        int row = grid.length;
        int col = grid[0].length;
        
        for(int i = 0; i < row; i ++){
            for(int j = 0; j < col; j++){
                int left = (j - 1 < 0) ? Integer.MAX_VALUE : dp[i][j-1];
                int top = (i - 1 < 0) ? Integer.MAX_VALUE : dp[i -1][j];
                if(i == 0 && j == 0) dp[i][j] = grid[i][j];
                else if(i == 0) dp[i][j] = left + grid[i][j];
                else if(j == 0) dp[i][j] = top + grid[i][j];
                else dp[i][j] = Math.min(left,top) + grid[i][j];
            }
        }
        return dp[row-1][col-1];       
        
    }
}