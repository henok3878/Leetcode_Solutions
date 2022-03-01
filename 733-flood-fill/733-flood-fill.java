class Solution {
    int[][] directions = new int[4][2];
       
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        
        directions[0] = new int[]{-1,0}; directions[1] = new int[]{0,1};
        directions[2] = new int[]{1,0}; directions[3] = new int[]{0,-1};
        
        Set<String> visited = new HashSet<>();
        
        dfs(image,sr,sc,image[sr][sc],newColor,visited);
        
        return image;
    }
    
    private void dfs(int[][] image, int sr, int sc,int color,  int newColor,Set<String> visited){
        String key = getKey(sr,sc);
        if(visited.contains(key)) return;
        visited.add(key);
        if(image[sr][sc] == color)
        {
            image[sr][sc] = newColor;
      
            for(int[] dir : directions){
                int i = sr+dir[0], j = sc + dir[1];
                if(i < 0 || i >= image.length || j < 0 || j >= image[0].length) continue;
                String k = getKey(i,j);
                if(!visited.contains(k))
                    dfs(image,i,j,color, newColor,visited);
                
            }
        }
        
    }
    
    private String getKey(int sr, int sc){
        return sr+","+sc;
    }
}