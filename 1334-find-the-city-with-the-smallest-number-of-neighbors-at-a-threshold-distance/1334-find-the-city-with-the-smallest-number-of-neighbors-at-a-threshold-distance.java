class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0; i < n ; i++) graph.add(new ArrayList<>());
        
        for(int[] edge : edges){
            graph.get(edge[0]).add(new int[]{edge[1],edge[2]});
            graph.get(edge[1]).add(new int[]{edge[0],edge[2]});
        }
        
        int[] rechable = new int[n];
        for(int i = 0; i < n; i++)
            rechable[i] = dijk(i,n,graph,distanceThreshold);
        
        //System.out.println(rechable);
        
        int min = n;
        int idx = -1;
        for(int i = 0; i < n;i++){
            if(min >= rechable[i]){
                min = rechable[i];
                idx = i;
            }
        }
        
        return idx;
        
    }
    
    private int dijk(int st,int n, List<List<int[]>> graph, int th){
        
    
        int[] dist = new int[n];
        Arrays.fill(dist,Integer.MAX_VALUE);
        dist[st] = 0;
        
        Queue<int[]> pq = new PriorityQueue<int[]>((a,b) -> a[1] - b[1]);
        pq.add(new int[]{st,0});
        
        while(!pq.isEmpty()){
            int[] curr = pq.poll();
            
            for(int[] adj : graph.get(curr[0])){
                if(dist[adj[0]] > curr[1] + adj[1]){
                    dist[adj[0]] = curr[1] + adj[1];
                    pq.add(new int[]{adj[0],dist[adj[0]]});
                }
            }
        }
        
        int count = 0;
        for(int d : dist) count += (d <= th) ? 1 : 0;
        
        return count;
        
    }
}