class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0;i < numCourses; i++)
            graph.add(new ArrayList<>());
        
        for(int[] pre : prerequisites){
            int u  = pre[0] , v = pre[1];
            graph.get(v).add(u);
            indegree[u]++;
        }
        int count = 0;
        Queue<Integer> q = new LinkedList<>();
        for(int i = 0; i < numCourses; i++){
             if(indegree[i] == 0) 
                q.add(i);
        }
           
        while(!q.isEmpty()){
            int curr = q.poll();
            count++;
            for(int adj : graph.get(curr)){
                if(--indegree[adj] == 0)
                    q.add(adj);
            }
        }
        
        return count == numCourses;
    }
}

/*

prereq[i] = [ai,bi] : bi -> ai

*/