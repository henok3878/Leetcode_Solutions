class Solution {
    
    public int networkDelayTime(int[][] times, int n, int k) {
        if(n < 2) return 0;
        List<List<int[]>> graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) graph.add(new ArrayList<int[]>());
        
        for(int[] edge : times){
            graph.get(edge[0]).add(new int[]{edge[1],edge[2]});
        }
        int[] distance = new int[n+1];
        Arrays.fill(distance,Integer.MAX_VALUE);
        distance[k] = 0;
        boolean[] visited = new boolean[n+1];
        Queue<int[]> queue = new PriorityQueue<>((a,b)->a[1] - b[1]);
        queue.add(new int[]{k,0});
        while(!queue.isEmpty()){
            int[] curr = queue.poll();
            visited[curr[0]] = true;
            for(int[] adj : graph.get(curr[0])){
                if(!visited[adj[0]]){
                    int currDist = curr[1] + adj[1];
                    if(distance[adj[0]] > currDist){
                        distance[adj[0]] = currDist;
                        queue.add(new int[]{adj[0],currDist});
                    }
                }
            }
        }
        int time = 0;
        for(int i = 1; i  <= n ; i++){
            int t = distance[i];
            if(t == Integer.MAX_VALUE) return -1;
            time = Math.max(time,t);
        }
        return time;
    }
}