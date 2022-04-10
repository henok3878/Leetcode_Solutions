class Solution {
    
    int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    
    public int longestIncreasingPath(int[][] matrix) {
        
        int m = matrix.length, n = matrix[0].length;
        int max = Integer.MIN_VALUE;
        int[][] dp = new int[m][n];
        for(int i  = 0 ; i < m ; i++){
            for(int j = 0; j < n; j++){
                max = Math.max(dfs(i,j,dp,matrix),max);
            }
        }
        
        return max + 1;
    }
    
    private int dfs(int i, int j, int[][] v, int[][] matrix){
        if(outBound(i,j,matrix.length,matrix[0].length))
            return 0;
        if(v[i][j] != 0)
            return v[i][j];
        int res = 0;
        for(int[] dir : directions){
            int x = i + dir[0], y = j + dir[1];
            if(!outBound(x,y,matrix.length,matrix[0].length) && matrix[i][j] < matrix[x][y])
                res = Math.max(res,1 + dfs(x,y,v,matrix));
        }
        return v[i][j] = res;
    }
    
    private boolean outBound(int i ,int j , int m , int n){
        return i < 0 || j < 0 || i >= m || j >= n;
    }
}

