class Solution {
    
    int[][] directions = {{0,1},{0,-1},{1,0},{-1,0}}; 

    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length , n = mat[0].length;
        
        Queue<int[]> queue = new LinkedList<>();

        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++){
                if(mat[i][j] == 1) mat[i][j] = -1;
                else if(mat[i][j] == 0 ) queue.add(new int[]{i,j});
            }
            
        
        int level = 0;
        while(!queue.isEmpty()){
            level++;
            int size = queue.size();
            for(int el = 0; el < size;el++){
                int[] curr = queue.poll();
                int i = curr[0], j = curr[1];
                for(int[] dir : directions){
                    int x = i + dir[0], y = j + dir[1];
                    if(x < 0 || y < 0 || x >= m || y >= n) continue;
                    if(mat[x][y] == -1){
                        queue.add(new int[]{x,y});
                        mat[x][y] = level;
                    }
                }
            } 
        }
        
        return mat;
        
    }

}