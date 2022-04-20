class Solution {
    
    int NOT_VISITED = 0;
    int VISITING = 1;
    int VISITED = 2;
    
    public int maximumInvitations(int[] favorite) {
        int n = favorite.length;
        
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0;i < n; i++)
            graph.add(new ArrayList<>());
        
        for(int i = 0;i < n; i++){
            graph.get(favorite[i]).add(i);
        }
        
        int longestCycle = 0;
        int longestChain = 0;
        int[] visited = new int[n];
        int[] depth = new int[n];
        Arrays.fill(depth,-1);
        
        for(int i = 0; i < n; i++){
            if(visited[i] == 0){
                int cycle = findCycle(i,graph,visited,0);
                if(cycle == 2){
                    int left = longestChain(favorite[i],i,graph,depth);
                    int right = longestChain(i,favorite[i],graph,depth);       
                    longestChain += left + right;
                }
                longestCycle = Math.max(longestCycle,cycle);
                }
        }
        //System.out.println(longestCycle + " : " + longestChain);
    
        return Math.max(longestCycle,longestChain);
        
    }
    
    private int longestChain(int p, int n,List<List<Integer>> graph, int[] depth){
        if(depth[n] != -1)
            return depth[n];
        depth[n] = 1;
        int dep = 1;
        for(int adj : graph.get(n)){
            if(adj == p) continue;
            dep = Math.max(dep,1 + longestChain(p,adj,graph,depth));
        }
        
        return depth[n] = dep;
    }
    
    private int findCycle(int n, List<List<Integer>> graph, int[] visited, int leng){
        if(visited[n] == VISITING)
            return leng;
        else if(visited[n] == VISITED)
            return Integer.MIN_VALUE;
        
        visited[n] = VISITING;
        int res = 0;
        for(int adj : graph.get(n)){
            res = Math.max(findCycle(adj,graph,visited,leng + 1), res);
        }
        visited[n] = VISITED;
        return res;
    }
}