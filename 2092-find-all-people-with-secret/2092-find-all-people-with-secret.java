class Solution {
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson)     {
        
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0;i < n; i++) graph.add(new ArrayList<>());
        
        graph.get(0).add(new int[]{firstPerson,0});
        graph.get(firstPerson).add(new int[]{0,0});
        
        for(int[] meeting : meetings){
            int x = meeting[0], y = meeting[1], t = meeting[2];
            graph.get(x).add(new int[]{y,t});
            graph.get(y).add(new int[]{x,t});
        }
        long[] dist = dijkstra(0,n,graph);
                
        List<Integer> ans = new ArrayList<>();
        for(int i = 0; i < n;i++){
            if(dist[i] < Long.MAX_VALUE)
                ans.add(i);
        }
        
        return ans;
    }
    
    private long[] dijkstra(int st, int n,List<List<int[]>> graph){
        long[] dist = new long[n];
        
        Arrays.fill(dist,Long.MAX_VALUE);
        dist[st] = 0;
        Queue<long[]> q = new PriorityQueue<>((a,b)-> (int)(a[1] - b[1]));
        q.add(new long[]{st,0});
        boolean[] visited = new boolean[n];
        
        while(!q.isEmpty()){
            long[] curr = q.poll();
            if(visited[(int)curr[0]]) continue;
            
            visited[(int)curr[0]] = true;
            for(int[] adj : graph.get((int)curr[0])){
                if(!visited[adj[0]] && dist[(int)adj[0]] > adj[1] && adj[1] >= curr[1]){
                    dist[(int)adj[0]] = adj[1];
                    q.add(new long[]{adj[0],adj[1]});
                }
            }
        }
        return dist;
    }
    
}

/*
When a meeting takesplace, 
    if either of participant have the secret, share 
    
How to know if participant has the secret?

The Most Challenging part: 
    - How to spread a screat instantaneously. (sharing it with people in the other meetings instantly)

4hrs sofar 

*/