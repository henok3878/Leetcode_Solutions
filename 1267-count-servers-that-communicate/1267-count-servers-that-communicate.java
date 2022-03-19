class Solution {
    
    int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
        
    public int countServers(int[][] grid) {
        
        int m = grid.length, n = grid[0].length;
        int ans = 0;
        
        for(int i = 0; i < m; i++){
            for(int j = 0;j < n ;j++){
                
                if(grid[i][j] == 1){
                    int res = dfs(i,j,grid);
                    ans += (res > 1 ) ? res : 0;
                }
            }
        }
        
        return ans;
        
    }
    
    
    private int dfs(int i , int j, int[][] grid){
        int m = grid.length; int n = grid[0].length;
        if(i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == 0) return 0;
        int res = 1;
        grid[i][j] = 0; // mark visited 
        
        for(int y = 0; y < n; y++){
            res += dfs(i,y,grid);
        }
        for(int x = 0; x < m; x ++){
            res += dfs(x,j,grid);
        }
        
        return res;
        
    }
}

/*
    1st Appr: 
        Do dfs on each cell that contains 1 


*/