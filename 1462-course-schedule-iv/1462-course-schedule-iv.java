class Solution {
    public List<Boolean> checkIfPrerequisite(int n, int[][] prerequisites, int[][] queries) {
        List<List<Integer>> graph = new ArrayList<>();
        List<Set<Integer>> prereqs = new ArrayList<>();

        for(int i = 0; i < n; i++){
            graph.add(new ArrayList<>());
            prereqs.add(new HashSet<>());
        }
        for(int[] pair : prerequisites){
            graph.get(pair[0]).add(pair[1]);
        }
        
        //System.out.println(graph);
        for(int i = 0;i  < n; i++){
            dfs(i,graph,prereqs);
        }
        
        //System.out.println(prereqs);
        
        List<Boolean> ans = new ArrayList<>();
                
        for(int i = 0; i < queries.length; i++){
            int[] q = queries[i];
            if(prereqs.get(q[0]).contains(q[1]))
                ans.add(true);
            else ans.add(false);
        }
        
        return ans;
    }
    
    private void dfs(int n, List<List<Integer>> graph, List<Set<Integer>> prereqs){
        if(!prereqs.get(n).isEmpty()) return;
        for(int adj : graph.get(n)){
            prereqs.get(n).add(adj);
            dfs(adj,graph,prereqs);
            if(!prereqs.get(adj).isEmpty()){
                prereqs.get(n).addAll(prereqs.get(adj));
            }
        }
    }
    
    
}