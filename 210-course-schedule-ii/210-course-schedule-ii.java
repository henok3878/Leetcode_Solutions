class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        Map<Integer,List<Integer>> graph = new HashMap<>();
        for(int i = 0; i < numCourses; i++) graph.put(i,new ArrayList<>());
        
        for(int[] pair : prerequisites){
            graph.get(pair[1]).add(pair[0]);
        }
        Boolean[] visited = new Boolean[numCourses];
        
        List<Integer> tempAns = new LinkedList<>();
        
        for(int i = 0; i < numCourses; i++)
            if(!dfs(i,visited,tempAns,graph)) 
                return new int[]{};
        
        int[] ans = new int[numCourses];
        for(int i = 0; i < numCourses; i++) ans[i] = tempAns.get(i);
        
        return ans;
    }
    
    private boolean dfs(int i,Boolean[] visited, List<Integer> ans, Map<Integer,List<Integer>> graph){
        if(visited[i] != null) return visited[i];
        
        visited[i] = false;
        for(int adj : graph.get(i)){
            if(!dfs(adj,visited,ans,graph)) return false;
        }
        ans.add(0,i);
        return visited[i] = true;
        
    }
}