class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        Map<Integer,List<Integer>> graph = new HashMap<>();
        List<List<Integer>> ans = new ArrayList<>();

        for(int i = 0;i < n; i++) {
            ans.add(new ArrayList<>());
            graph.put(i, new ArrayList<>());
        }
        
        for(int[] edge : edges){
            graph.get(edge[0]).add(edge[1]);
        }
        
        for(int i = 0; i < n; i++)
            dfs(i,i,ans,graph);
        
        return ans;
        
    }
    
    private void dfs(int x, int curr, List<List<Integer>> ans, Map<Integer,List<Integer>> graph) {
    for (int ch: graph.get(curr))
        if(ans.get(ch).size() == 0 || ans.get(ch).get(ans.get(ch).size() - 1) != x) {
            ans.get(ch).add(x);
            dfs(x, ch, ans, graph);
        }
}
}