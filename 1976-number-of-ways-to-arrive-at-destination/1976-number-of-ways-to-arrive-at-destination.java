class Solution {
    int MOD = 1_000_000_007;
    public int countPaths(int n, int[][] roads) {
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0;i < n; i++) graph.add(new ArrayList<>());
        
        for(int[] road : roads){
            int u = road[0], v = road[1], cost = road[2];
            graph.get(u).add(new int[]{v,cost});
            graph.get(v).add(new int[]{u,cost});
        }
        
        boolean[] visited = new boolean[n];
        long[] dis = new long[n];
        Arrays.fill(dis,Long.MAX_VALUE);
        dis[0] = 0;
        Queue<long[]> queue = new PriorityQueue<long[]>((a,b) -> (int)(a[1] - b[1]));
        queue.add(new long[]{0,0});
        visited[0] = true;
        
        while(!queue.isEmpty()){
            long[] curr = queue.poll();
            visited[(int)curr[0]] = true;
            for(int[] adj : graph.get((int)curr[0])){
                if(dis[adj[0]] > (adj[1] + curr[1])){
                    dis[adj[0]] = adj[1] + curr[1];
                    queue.add(new long[]{adj[0],dis[adj[0]]});
                }
            }
        }
        
        long s = dis[n-1];
        //System.out.println(s);
        
        long[] dp = new long[n];
        
        int ans =  (int)((dfs(-1,0,n-1,0,s,graph,new boolean[n],dp,dis))%MOD);
        //System.out.println(Arrays.toString(dp));
        return ans;
    }
    
    private long dfs(int p, int st, int end, long cost, long shrt, List<List<int[]>> graph, boolean[] v,long[] dp, long[] dis){
        // System.out.println(p + "->" + st + " cost: " + cost + " dp:  " + Arrays.toString(dp) + " v[st]: " + v[st]);
        if(st == end)
            return 1;
        if(v[st]) return dp[st] % MOD;
        v[st] = true;
        long res = 0;        
        for(int[] adj : graph.get(st)){
            if(cost + adj[1] > dis[adj[0]]) continue;
            res += dfs(st,adj[0],end,cost + adj[1],shrt,graph,v,dp,dis);
            res %= MOD;
     
        }
        return dp[st] = res;
    }
}

/*
    Dijkstera
    Do dfs with path pruning 


*/