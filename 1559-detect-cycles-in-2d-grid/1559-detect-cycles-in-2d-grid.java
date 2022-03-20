class Solution {
    
    int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    public boolean containsCycle(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
            
        for(int i = 0; i < m; i++){
            for(int j = 0;j < n; j++){
                if(!visited[i][j] && isCycleFound(i,j,i,j,visited,grid))
                    return true;
            }
        }
        return false;
    }
    
    private boolean isCycleFound(int currX,int currY, int parX,int parY, boolean[][] visited, char[][] grid){

        if(currX < 0 || currY < 0 || currX >= grid.length || currY >= grid[0].length || grid[parX][parY] != grid[currX][currY])
            return false;
        
        if(visited[currX][currY] && grid[currX][currY] == grid[parX][parY]) return true;
        else if(visited[currX][currY]) return false;
        
        visited[currX][currY] = true;
        
        for(int[] dir : directions){
            int x = currX + dir[0], y = currY + dir[1];
            if(!( x == parX && y == parY) && isCycleFound(x,y,currX,currY,visited,grid)) return true;
        }
        
        return false;
        
    }
}