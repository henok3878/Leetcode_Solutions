class Solution {
    
    int[][] directions = new int[4][2];

    public int maxAreaOfIsland(int[][] grid) {
        directions[0] = new int[]{-1,0}; directions[1] = new int[]{0,1};
        directions[2] = new int[]{1,0}; directions[3] = new int[]{0,-1};
        
        int ans = 0;
        Set<String> visited = new HashSet<>();
        
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 1 && !visited.contains(getKey(i,j))){
                    ans = Math.max(ans,dfs(i,j,visited,grid));
                }
                
            }
        }
        
        return ans;
    }
    
    private int dfs(int i , int j,Set<String> visited, int[][] grid){
        String key = getKey(i,j);
        if(grid[i][j] == 0 || visited.contains(key)) return 0;
        
        visited.add(key);
        int ans = 1;
        for(int[] dir : directions){
            int x = i + dir[0], y = j + dir[1];
            if(x < 0 || y < 0 || x >= grid.length || y >= grid[0].length) continue;
            ans += dfs(x,y,visited,grid);
            
        }
        return ans;
        
    }
    
    String getKey(int i, int j){
        return i +","+j;
    }
    
}

/*
st: 3:38 
1st test: 3:49 


*/