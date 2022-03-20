class Solution {
    
    int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    public boolean containsCycle(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] visited = new int[m][n];
        for(int i = 0; i < m; i++) Arrays.fill(visited[i],-1);
            
        for(int i = 0; i < m; i++){
            for(int j = 0;j < n; j++){
                if(visited[i][j] == -1 && isCycleFound(i,j,i,j,visited,grid))
                    return true;
            }
        }
        return false;
    }
    
    private boolean isCycleFound(int currX,int currY, int parX,int parY, int[][] visited, char[][] grid){
        int n = grid[0].length;
        int currId = currX*n + currY;
        int parId = parX*n + parY;
        if(currX < 0 || currY < 0 || currX >= grid.length || currY >= grid[0].length || grid[parX][parY] != grid[currX][currY])
            return false;
        
        if(visited[currX][currY] != -1 && visited[parX][parY] != currId) return true;
        else if(visited[currX][currY] != -1) return false;
        
        visited[currX][currY] = parId;
        
        for(int[] dir : directions){
            int x = currX + dir[0], y = currY + dir[1];
            if(isCycleFound(x,y,currX,currY,visited,grid)) return true;
        }
        
        return false;
        
    }
}