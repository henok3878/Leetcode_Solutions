class Solution {
    int MOD;
    public int countRestrictedPaths(int n, int[][] edges) {
        MOD = (int)Math.pow(10,9) + 7;
        
        int[] shortestDist = new int[n+1];
        Arrays.fill(shortestDist,Integer.MAX_VALUE);
        boolean[] visited = new boolean[n+1];
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        
        for(int[] edge : edges){
            graph.get(edge[0]).add(new int[]{edge[1],edge[2]});
            graph.get(edge[1]).add(new int[]{edge[0],edge[2]});   
        }
        
        Queue<int[]> pq = new PriorityQueue<>((a,b)->a[1] - b[1]);
        shortestDist[n] = 0;
        pq.add(new int[]{n,0});
        
        while(!pq.isEmpty()){
            int[] curr = pq.poll();
            visited[curr[0]] = true;
            
            for(int[] adj : graph.get(curr[0])){
                if(!visited[adj[0]] && shortestDist[adj[0]] > curr[1] + adj[1]){
                    shortestDist[adj[0]] = curr[1] + adj[1];
                    pq.add(new int[]{adj[0],shortestDist[adj[0]]});
                }
            }
        }
        int[] dp = new int[n+1];
        Arrays.fill(dp,-1);
        return dfs(1,n,graph,shortestDist,dp) % MOD;
        
    }
    
    
    private int dfs(int i,int n,List<List<int[]>> graph,int[] shortest,int[] dp){
        if(i == n){
            return 1;
        }
        else if(dp[i]  != -1) return dp[i];
        int ans = 0;
        for(int[] adj : graph.get(i)){
            if(shortest[adj[0]] < shortest[i]){
                ans += dfs(adj[0],n,graph,shortest,dp);
                ans %= MOD;
            }
        }
        return dp[i] = ans;
    }
}