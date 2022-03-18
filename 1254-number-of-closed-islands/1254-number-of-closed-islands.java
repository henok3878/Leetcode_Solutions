class Solution {
    int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    
    public int closedIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int numOfIslands = 0;
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(grid[i][j] == 0 && dfs(i,j,grid)) numOfIslands++;
            }
        }
        
        return numOfIslands;
        
        
    }
    
    private boolean dfs(int row, int col, int[][] grid){
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length)
            return false;
        else if(grid[row][col] == 1) return true;
        grid[row][col] = 1; // mark as visited 
        boolean res = true;
        for(int[] dir : directions){
            int x  = row + dir[0], y = col + dir[1];
            if(!dfs(x,y,grid)) res = false;
        }
        return res;
    } 
}

/*
    1st Approch: DFSS 
        - for every land, do a dfs 
            if(out of bound) return false;
            else if(grid[i][j] == 1) return true;
            else 
                for(each adj cell)
                    // do dfs
                    if(!dfs()) return false;
                return true;
        

[0,0,1,1,0,1,0,0,1,0],
[1,1,0,1,1,0,1,1,1,0],
[1,0,1,1,1,0,0,1,1,0],
[0,1,1,0,0,0,0,1,0,1],
[0,0,0,0,0,0,1,1,1,0],
[0,1,0,1,0,1,0,1,1,1],
[1,0,1,0,1,1,0,0,0,1],
[1,1,1,1,1,1,0,0,0,0],
[1,1,1,0,0,1,0,1,0,1],
[1,1,1,0,1,1,0,1,1,0]]



*/