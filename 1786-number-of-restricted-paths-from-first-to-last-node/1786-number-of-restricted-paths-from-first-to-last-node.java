class Solution {
    int MOD = 1_000_000_007;
    
    public int countRestrictedPaths(int n, int[][] edges) {
        
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++)
            graph.add(new ArrayList<>());
        for(int[] edge : edges){
            graph.get(edge[0]).add(new int[]{edge[1],edge[2]});
            graph.get(edge[1]).add(new int[]{edge[0],edge[2]});
        }
        
        int[] dist = new int[n + 1];
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[n] = 0;
        
        Queue<int[]> q = new PriorityQueue<int[]>((a,b) -> a[1] - b[1]);
        q.add(new int[]{n,0});
        while(!q.isEmpty()){
            
            int[] curr = q.poll(); // curr node has got its min distance so you can mark here as a visited 
            for(int[] adj : graph.get(curr[0])){
                if(dist[curr[0]] + adj[1] < dist[adj[0]]){
                    dist[adj[0]] = dist[curr[0]] + adj[1];
                    q.add(new int[]{adj[0],dist[adj[0]]});
                }
            }
        }
        
        int[] dp = new int[n+1];
        Arrays.fill(dp,-1);
        dfs(1,n,graph,dist,dp);
        return dp[1] % MOD;
    }
    
    private int dfs(int i, int n, List<List<int[]>> graph,int[] dist, int[] dp){
        if(i == n)
            return 1;
        else if(dp[i] != -1)
            return dp[i];
        
        int res = 0;
        for(int[] adj : graph.get(i)){
            if(dist[i] > dist[adj[0]]){
                res += dfs(adj[0],n,graph,dist,dp);
                res %= MOD;
            }
        }
        return dp[i] = res;
    }
}

/*

find shortest path from node n to all other nodes: 
start dfs from node 1 and traverse down the graph as long as prev node's dis is greater that current node.

*/