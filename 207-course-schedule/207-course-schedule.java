class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        
        Map<Integer,List<Integer>> graph = new HashMap<>();
        Boolean[] visited = new Boolean[numCourses];
        for(int i = 0; i < numCourses; i++) graph.put(i,new ArrayList<>());
        
        for(int [] pair : prerequisites)
            graph.get(pair[1]).add(pair[0]);
        
        for(int i = 0; i < numCourses; i++)
            if(visited[i] == null && !canFinishHelper(i,visited,graph))
                return false;
        
        return true;
        
    }
    
    private boolean canFinishHelper(int i,Boolean[] visited, Map<Integer,List<Integer>> graph){
        if(visited[i] != null) return visited[i];
        visited[i] = false;
        for(int adj : graph.get(i)){
            if(!canFinishHelper(adj,visited,graph))
                return false;
        }
        return visited[i] = true;
    }
    
}

/*
    if the path already visited-> return true
    else if the path is in the current path -> return false
    //add this node to current path
    visted[curr] = false;
    for each adj of curr node 
        if(!explore(adj)) return false
    return visited[curr] = true;
    
    

*/