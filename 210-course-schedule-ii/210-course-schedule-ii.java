class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        
        for(int[] pair : prerequisites){
            int u = pair[0], v = pair[1];
            graph.get(v).add(u);
        }
        
        Boolean[] visited = new Boolean[numCourses];
        List<Integer> ans = new ArrayList<>();
        for(int i = 0; i < numCourses; i++) 
            if(!dfs(i,visited,ans,graph))
                return new int[]{};
        int[] res = new int[numCourses];
        for(int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
        
    }
    
    private boolean dfs(int curr, Boolean[] visited, List<Integer> ans, List<List<Integer>> graph){
        if(visited[curr] != null) return visited[curr];
        
        visited[curr] = false;
        
        for(int adj : graph.get(curr))
            if(!dfs(adj,visited,ans,graph))
                return false;
        
        ans.add(0,curr);
        return visited[curr] = true;
            
    }
    
}