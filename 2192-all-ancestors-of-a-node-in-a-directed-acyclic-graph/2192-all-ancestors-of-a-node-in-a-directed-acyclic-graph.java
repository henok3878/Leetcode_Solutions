class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        List<List<Integer>> graph = new ArrayList<>();
        List<List<Integer>> ans = new ArrayList<>();

        for(int i = 0;i < n; i++){
            graph.add(new ArrayList<>());
            ans.add(new ArrayList<>());
        }
        for(int[] edge : edges)
            graph.get(edge[0]).add(edge[1]);
        
        for(int i = 0; i < n; i++){
            dfs(i,i,graph,ans);
        }
        
        return ans;
    }
    
    private void dfs(int p, int n, List<List<Integer>> graph, List<List<Integer>> ans){
        
        for(int adj : graph.get(n)){
            int size = ans.get(adj).size();
            if(size == 0 || ans.get(adj).get(size - 1) != p){
                ans.get(adj).add(p);
                dfs(p,adj,graph,ans);
            }
        }
    }
}