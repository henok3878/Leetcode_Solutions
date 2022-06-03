class NumMatrix {
    int[][] prefixSum;
    public NumMatrix(int[][] matrix) {
        prefixSum = new int[matrix.length][matrix[0].length + 1];
        for(int i = 0; i < matrix.length; i++){
            for(int j = 1; j < prefixSum[0].length;j++){
                prefixSum[i][j] = prefixSum[i][j-1] + matrix[i][j-1];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        
        int sum = 0;
        for(int row = row1; row <= row2; row++){
            sum += prefixSum[row][col2 + 1] - prefixSum[row][col1];
        }
        
        return sum;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */