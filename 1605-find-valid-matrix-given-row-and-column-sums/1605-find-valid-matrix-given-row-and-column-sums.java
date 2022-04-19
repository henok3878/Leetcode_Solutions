class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int rows = rowSum.length, cols = colSum.length;
        int[][] ans = new int[rows][cols];
        
        for(int i = 0; i < rows ; i++){
            for(int j = 0; j < cols; j++){
                ans[i][j] = Math.min(rowSum[i],colSum[j]);
                rowSum[i] -= ans[i][j];
                colSum[j] -= ans[i][j];
            }
        }
        
        return ans;
        
    }
}