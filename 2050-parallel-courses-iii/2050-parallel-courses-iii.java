class Solution {
    public int minimumTime(int n, int[][] relations, int[] time) {
        
        boolean[] visited = new boolean[n+1];
        int[] timeNeeded = new int[n+1];
        
        Map<Integer,List<Integer>> graph = new HashMap<>();
        
        for(int i = 1;i <= n;i++){
            graph.put(i,new ArrayList<>());
        }
        
        for(int[] relation : relations){
            graph.get(relation[1]).add(relation[0]);
        }
        
        int ans = Integer.MIN_VALUE;
        for(int i = 1; i<= n; i++){
            
            ans = Math.max(ans,dfs(i,visited,timeNeeded,time,graph));
        }
        
        return ans;
    
    }
    
    private int dfs(int i,boolean[] visited,int[] timeNeeded,int[] time, Map<Integer,List<Integer>> graph){
        if(visited[i]) return timeNeeded[i];
        else if(graph.get(i).size() == 0) return time[i-1];
        visited[i] = true;
        int max = Integer.MIN_VALUE;
        for(int adj : graph.get(i)){
            max = Math.max(max,dfs(adj,visited,timeNeeded,time,graph));
        }
        
        return timeNeeded[i] = time[i - 1] + max;
    }
}