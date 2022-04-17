class Solution {
    public int minimumTime(int n, int[][] relations, int[] time) {
        int[] indegree = new int[n + 1];
        List<List<Integer>> graph = new ArrayList<>();
        
        for(int i = 0; i <= n; i++){
            graph.add(new ArrayList<>());
        }
        
        for(int[] relation : relations){
            graph.get(relation[0]).add(relation[1]);
            indegree[relation[1]]++;
        }
        
        Queue<Integer> q = new LinkedList<>();
        for(int i = 1; i <= n ; i++){
            if(indegree[i] == 0) q.add(i);
        }
        
        int[] compTime = new int[n+1];
        
        int ans = -1;
        
        while(!q.isEmpty()){
            int curr = q.poll();
            compTime[curr] += time[curr-1];
            ans = Math.max(ans,compTime[curr]);
            
            for(int adj : graph.get(curr)){
                
                compTime[adj] = Math.max(compTime[adj],compTime[curr]);
                if(--indegree[adj] == 0)
                    q.add(adj);
                // System.out.println("curr: " + curr + " adj: " + adj + " " + Arrays.toString(compTime));
            }
        }
        return ans;
    }
}