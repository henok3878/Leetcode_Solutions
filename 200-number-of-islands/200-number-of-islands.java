class Solution {
    
    int[][] directions = {{-1,0},{0,1},{1,0},{0,-1}};
    
    public int numIslands(char[][] grid) {
        int islands  = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '1'){
                    islands++;
                    dfs(i,j,grid);
                }
            }
        }
        
        return islands;
    }
    
    private void dfs(int i, int j, char[][] grid){
        if(i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != '1') return;
        grid[i][j] = '*';
        for(int[] dir : directions){
            dfs(i + dir[0],j + dir[1],grid);
        }
    }
}

/*
st: 5:28 

sub: 

*/