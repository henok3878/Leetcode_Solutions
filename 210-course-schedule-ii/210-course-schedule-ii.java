class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        
        Map<Integer,List<Integer>> graph = new HashMap<>();
        for(int i = 0; i < numCourses; i++) graph.put(i,new ArrayList<>());
        
        int[] indegree = new int[numCourses];
        
        for(int[] pair : prerequisites){
            graph.get(pair[1]).add(pair[0]);
            indegree[pair[0]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < numCourses; i++)
            if(indegree[i] == 0) queue.add(i);
        int visited = 0;
        int[] ans = new int[numCourses];
        
        while(!queue.isEmpty()){
            int curr = queue.poll();
            ans[visited++] = curr;
            for(int adj : graph.get(curr))
                if(--indegree[adj] == 0) queue.add(adj);
        }
        
        return (visited == numCourses) ? ans : new int[]{};
        
    }
}