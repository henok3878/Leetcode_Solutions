class Solution {
    
    int VISITED = 2, VISITING = 1, NOT_VISITED = 0;
    
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        
        int[] visited = new int[n];
        List<Integer> ans = new ArrayList<>();
        
        for(int i = 0; i < n; i++){
            if(dfs(i,visited,ans,graph)){
                ans.add(i);
            }  
        }
        
        return ans;
        
    }
    
    private boolean dfs(int n, int[] visited, List<Integer> ans,int[][] graph){
        if(visited[n] != NOT_VISITED)
            return visited[n] == VISITED;
        visited[n] = VISITING;
        for(int adj : graph[n]){
            if(!dfs(adj,visited,ans,graph))
                return false;
        }
        visited[n] = VISITED;
        return true;
    }
}