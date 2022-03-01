class Solution {
    int[][] directions = new int[4][2];
       
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        
        directions[0] = new int[]{-1,0}; directions[1] = new int[]{0,1};
        directions[2] = new int[]{1,0}; directions[3] = new int[]{0,-1};
                
        dfs(image,sr,sc,image[sr][sc],newColor);
        
        return image;
    }
    
    private void dfs(int[][] image, int sr, int sc,int color,  int newColor){

        if(image[sr][sc] == color && image[sr][sc] != newColor) 
        // checks if it's not visited and same color with starting cell 
        {
            image[sr][sc] = newColor; 
            // changes its color, also implicitly marks the cell visited
      
            for(int[] dir : directions){
                int i = sr+dir[0], j = sc + dir[1];
                if(i < 0 || i >= image.length || j < 0 || j >= image[0].length) continue;
                dfs(image,i,j,color, newColor);
                
            }
        }
        
    }

}

/*
    1) First implementation using Visited set: 
        - I used set to keep track of visited cells, but it is redundant becuase we are already changing 
        visited cells to a new color, so we can keep track of visited cells implcitly.

    2) Without using visited set:
*/