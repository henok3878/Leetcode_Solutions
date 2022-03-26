class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        
        List<List<double[]>> graph = new ArrayList<>();
        for(int i = 0 ; i < n; i++) graph.add(new ArrayList<>());
        
        for(int i = 0; i < edges.length; i++){
            int[] edge = edges[i];
            graph.get(edge[0]).add(new double[]{edge[1],succProb[i]});
            graph.get(edge[1]).add(new double[]{edge[0],succProb[i]});
        }
        
        double[] dist = new double[n];
        dist[end] = 1;
        
        Queue<double[]> pq = new PriorityQueue<double[]>((a,b)->Double.compare(b[1],a[1]));
        pq.add(new double[]{end,1.0});
        
        while(!pq.isEmpty()){
            double[] curr = pq.poll();
            double node = curr[0];
            double w = curr[1];
            for(double[] adj : graph.get((int)node)){
                if(dist[(int)adj[0]] < w * adj[1]){
                    dist[(int)adj[0]] = w * adj[1];
                    pq.add(new double[]{adj[0], dist[(int)adj[0]]});
                }
            }
        }
        return dist[start];
    }
}