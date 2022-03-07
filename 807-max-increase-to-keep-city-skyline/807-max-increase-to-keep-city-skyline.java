class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        int n = grid.length;
        int[] rowMax = new int[n];
        int[] colMax = new int[n];
        for(int i = 0; i < n; i++){
            int maxR = Integer.MIN_VALUE;
            int maxC = Integer.MIN_VALUE;
            for(int j = 0; j < n; j++){
                maxR = Math.max(maxR,grid[i][j]); 
                maxC = Math.max(maxC,grid[j][i]);
            }
            rowMax[i] = maxR;
            colMax[i] = maxC;
        }
        
        int totalSum = 0;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                totalSum += Math.min(rowMax[i], colMax[j]) - grid[i][j];
            
        return totalSum;
    }
}

/*
st: 2:17 

sub: 2:50 

*/