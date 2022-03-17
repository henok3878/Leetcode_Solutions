class Solution {
    int[][] directions = {{1,0},{0,1},{-1,0},{0,-1}};
    public int countSubIslands(int[][] grid1, int[][] grid2) {

        int m1 = grid1.length, n1 = grid1[0].length;
        int m2 = grid2.length, n2 = grid2[0].length;
        
        int count = 0;
        
        for(int i = 0; i < m2; i++){
            for(int j = 0; j < n2; j++){
                if(grid2[i][j] == 1 && grid1[i][j] == 1)
                    count += dfs(i,j,grid1,grid2) ? 1 : 0;
            }
        }
        
        return count;
        
    }
    
    private boolean dfs(int r, int c, int[][] grid1,int[][] grid2){
        if(r < 0 ||  c < 0 || r >= grid2.length || c >= grid2[0].length || grid2[r][c] != 1) return true;
        else if(grid1[r][c] != 1) return false;
        
        grid2[r][c] = -1; // -1 representing visited cells 
        
        boolean res = true;
        for(int[] dir : directions){
            int x = r + dir[0], y = c + dir[1];
            res &= dfs(x,y,grid1,grid2);
        }
        return res;
    }
    
}

/*
1st Approch: 
    - Find islands in grid2 (including their path)
    - Check if each island in a grid2 is included in grid1 (check using their path)
    
    Node = M*N
    Edges = 4*M*N
    
    traversing the grid = O(Node + Edges)
                        = O(M*N + M*N)
                        = O(M*N)
                        
Optimization: 
    - Remove 2nd step (traversal) 
*/