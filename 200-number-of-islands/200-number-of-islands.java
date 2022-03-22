class Solution {
    int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        
        int islands = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0;j < n; j++){
                if(grid[i][j] == '0') continue;
                dfs(i,j,grid);
                islands++;
            }
        }
        return islands;
    }
    
    private void dfs(int i, int j, char[][] grid){
        if(i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == '0') return;
        grid[i][j] = '0';
        for(int[] dir : directions){
            int x = i + dir[0], y = j + dir[1];
            dfs(x,y,grid);
        }
    }
    
}