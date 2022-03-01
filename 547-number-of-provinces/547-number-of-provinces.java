class Solution {
    public int findCircleNum(int[][] isConnected) {
        
        boolean[] visited = new boolean[isConnected.length];
            
        int ans = 0;
        
        for(int i = 0; i < isConnected.length; i++){
            // for each cell, call dfs 
            if(!visited[i]){
                ans++;
                dfs(i,visited,isConnected);
            }
        }
        
        return ans;
    }
    
    private void dfs(int i, boolean[] visited, int[][] graph){
        if(visited[i]) return;
        visited[i] = true;
        for(int city = 0; city < graph.length; city++){
            if(graph[i][city] == 1 ){
                dfs(city,visited,graph);
            }
        }
    }
}