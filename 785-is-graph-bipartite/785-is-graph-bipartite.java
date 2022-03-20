class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        
        int[] colors = new int[n+1];
        colors[n] = -1;
        
        for(int i = 0; i < n; i++){
            if(colors[i] == 0 && !dfs(i,n,colors,graph)) return false;    
        }
        
        return true;
    }
    
    private boolean dfs(int n,int p, int[] colors, int[][] graph){
        if(colors[n] != 0) return colors[p] != colors[n];

        colors[n] = -1 * colors[p]; // mark visited and also color the node
        for(int adj : graph[n])
            if(!dfs(adj,n,colors,graph)) return false;
        return true;
    }
}