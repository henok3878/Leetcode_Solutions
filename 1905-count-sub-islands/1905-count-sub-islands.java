class Solution {
    int[][] directions = {{1,0},{0,1},{-1,0},{0,-1}};
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        List<List<int[]>> grid2Islands = new ArrayList<>();
        int m1 = grid1.length, n1 = grid1[0].length;
        int m2 = grid2.length, n2 = grid2[0].length;
        
        for(int i = 0; i < m2; i++){
            for(int j = 0; j < n2; j++){
                List<int[]> island = new ArrayList<>();
                if(grid2[i][j] == 1){
                    dfs(i,j,grid2,island);
                    grid2Islands.add(island);
                }
            }
        }
        
        int count = 0;
        for(List<int[]> island : grid2Islands)
            if(dfs2(0,island,grid1)) count ++;
        
        return count;
        
    }
    
    private void dfs(int r, int c, int[][] grid, List<int[]> path){
        path.add(new int[]{r,c});
        grid[r][c] = -1; // -1 representing visited cells 
        for(int[] dir : directions){
            int x = r + dir[0], y = c + dir[1];
            if(x < 0 ||  y < 0 || x >= grid.length || y >= grid[0].length || grid[x][y] != 1) continue;
            dfs(x,y,grid,path);
        }
    }
    
    private boolean dfs2(int cellIdx, List<int[]> island, int[][] grid){
        if(cellIdx == island.size()) return true;
        int[] currCell = island.get(cellIdx);
        if(grid[currCell[0]][currCell[1]] == 0) return false;
        
        return dfs2(cellIdx + 1, island,grid);
    }
}

/*
1st Approch: 
    - Find islands in grid2 (including their path)
    - Check if each island in a grid2 is included in grid1 (check using their path)

*/