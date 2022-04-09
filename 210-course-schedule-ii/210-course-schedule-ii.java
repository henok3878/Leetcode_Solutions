class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] ans = new int[numCourses];
        int idx = 0;
        
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < numCourses; i++) 
            graph.add(new ArrayList<>());
        
        int[] indegree = new int[numCourses];
        
        for(int[] pre : prerequisites){
            int u = pre[0] , v = pre[1];
            graph.get(v).add(u);
            indegree[u]++;
        }
        
        Queue<Integer> q = new LinkedList<>();
        
        for(int i = 0; i < numCourses; i++){
            if(indegree[i] == 0)
                q.add(i);
        }
        
        while(!q.isEmpty()){
            int curr = q.poll();
            ans[idx++] = curr;
            for(int adj: graph.get(curr)){
                if(--indegree[adj] == 0){
                    q.add(adj);
                }
            }
        }
        
        return (idx == numCourses) ? ans : new int[0];
    }
}