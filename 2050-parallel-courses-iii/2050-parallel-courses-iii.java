class Solution {
    
    public int minimumTime(int n, int[][] relations, int[] time) {
        int[] timeNeeded = new int[n + 1];
        Map<Integer,List<Integer>> graph = new HashMap<>();
        
        for(int i = 1; i <= n; i++){
            timeNeeded[i] = time[i-1];
            graph.put(i,new ArrayList<>());
        }
        
        int[] indegree = new int[n+1];
            
        for(int[] pair : relations){
            graph.get(pair[0]).add(pair[1]);
            indegree[pair[1]]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        
        for(int i = 1; i <= n; i++) if(indegree[i] == 0) queue.add(i);
        
        int ans = Integer.MIN_VALUE;
        
        while(!queue.isEmpty()){
            int curr = queue.poll();
            ans = Math.max(timeNeeded[curr],ans);
            
            for(int adj: graph.get(curr)){
                if(--indegree[adj] == 0) 
                    queue.add(adj);
                timeNeeded[adj] = Math.max(time[adj-1] + timeNeeded[curr], timeNeeded[adj]);
            }
        }
        
        return ans;
    }
}