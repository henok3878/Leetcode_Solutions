class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        int rows = rowSum.length, cols = colSum.length;
        int[][] ans = new int[rows][cols];
        
        for(int i = 0; i < rows; i++){
            for(int j = 0;j < cols; j++){
                int min = Math.min(rowSum[i], colSum[j]);
                rowSum[i] -= min; colSum[j] -= min;
                ans[i][j] = min;
            }
        }
        
        return ans;
    }
}

/*
st: 3:23 


*/