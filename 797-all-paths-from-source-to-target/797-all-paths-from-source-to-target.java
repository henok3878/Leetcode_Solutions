class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        
        int n = graph.length;
        
        List<List<Integer>> ans = new ArrayList<>();
        
        dfs(0,n-1, graph,ans, new ArrayList<>());
        
        return ans;
        
    }
    
    private void dfs(int node, int target, int[][] graph, List<List<Integer>> ans, List<Integer> curr){
        
        curr.add(node);
        if(node == target){
            ans.add(new ArrayList<>(curr));
            curr.remove(curr.size() - 1);
            return;
        }        
        for(int n : graph[node]){
            dfs(n,target,graph,ans,curr);
        }
        curr.remove(curr.size() - 1);
    }
        
    
}

/*

*/