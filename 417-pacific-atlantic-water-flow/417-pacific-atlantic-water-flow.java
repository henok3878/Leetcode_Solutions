class Solution {
    int[][] directions = {{1,0},{-1,0},{0,1},{0,-1}};
    
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length , n = heights[0].length;
        Queue<int[]> queueA = new LinkedList<>();
        Queue<int[]> queueP = new LinkedList<>();
        boolean[][] atlantic = new boolean[m][n];
        boolean[][] pacific = new boolean[m][n];
        for(int i = 0; i < m; i++){
            queueA.add(new int[]{i,n - 1});
            queueP.add(new int[]{i,0});
            atlantic[i][n-1] = true;
            pacific[i][0] = true;
        }
        for(int j = 0; j < n; j++){
            queueA.add(new int[]{m-1,j});
            queueP.add(new int[]{0,j});
            atlantic[m-1][j] = true;
            pacific[0][j] = true;
        }
        bfs(queueA,heights,atlantic);
        bfs(queueP,heights,pacific);
        List<List<Integer>> ans = new ArrayList<>();
        
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(pacific[i][j] && atlantic[i][j]){
                    ans.add(Arrays.asList(i,j));
                }
            }
        }
        
        return ans;
        
        
    }
    
    private void bfs(Queue<int[]> queue, int[][] heights, boolean[][] visited){
           
        while(!queue.isEmpty()){
            int[] curr = queue.poll();
            int i = curr[0], j = curr[1];
            //System.out.println("x: " + i + " y: " + j);
            for(int[] dir : directions){
                int x = i + dir[0], y = j + dir[1];
                if(x < 0 || y < 0 || y >= heights[0].length || x >= heights.length || heights[i][j] > heights[x][y] || visited[x][y])
                    continue;
                queue.add(new int[]{x,y});
                visited[x][y] = true;
            }
        }
    }
}

/*
    adj >= curr  
    


*/