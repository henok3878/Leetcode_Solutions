class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] visited = new int[n];
        
        int pColor = -1;
        for(int node = 0; node < n; node++){
            if(visited[node] == 0 && !dfs(node,pColor,graph,visited))
                return false;
        }
        return true;
    }
    
    private boolean dfs(int node, int pColor, int[][] graph, int[] visited){
        int currColor = pColor * -1;
        visited[node] = currColor;
        for(int adj : graph[node]){
            if(visited[adj] != 0) {
                if(visited[adj] == currColor) return false; 
                continue;
            }
            if(!dfs(adj,currColor,graph,visited)) return false;
        }
        
        return true;
    }
}