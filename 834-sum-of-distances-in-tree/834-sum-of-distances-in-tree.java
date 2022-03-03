class Solution {
    int[] ans, count;
    List<List<Integer>> graph;
    int N;
    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        this.N = n;
        ans = new int[N];
        count = new int[N];
        Arrays.fill(count, 1);
        graph = new ArrayList<>();
        for(int i = 0; i < n; i++) graph.add(new ArrayList<>());
        
        for(int[] edge : edges){
            int u = edge[0], v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        
        dfs(0, new HashSet<Integer>());
        dfs2(0, new HashSet<Integer>());
        return ans;
    }
    
     public void dfs(int node, Set<Integer> visited) {
        visited.add(node);
        for (int child: graph.get(node))
            if(!visited.contains(child)){
                dfs(child, visited);
                count[node] += count[child];
                ans[node] += ans[child] + count[child];
            }
    }

    public void dfs2(int node, Set<Integer> visited) {
        visited.add(node);
        for (int child: graph.get(node))
            if (!visited.contains(child)) {
                ans[child] = ( ans[node] - count[child] ) + N - count[child];
                dfs2(child, visited);
            }
    }
}


/*
st: 1:17 

Keywords : undirected, n nodes, n - 1 edges 


answer[i] = sum of distances between ith node in the tree and all other nodes 



*/