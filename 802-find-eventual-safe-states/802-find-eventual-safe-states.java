class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        List<Integer> ans = new ArrayList<>();
        boolean[] res = new boolean[graph.length];
        Set<Integer> visited = new HashSet<>();
        for(int i = 0; i < graph.length; i++){
            if(dfs(i,visited,graph,res)) ans.add(i);   
        }
        return ans;
    }
    
    
    private boolean dfs(int node, Set<Integer> visited, int[][] graph,boolean[] res){
        if(visited.contains(node)) return res[node];
        int[] adjs = graph[node];
        visited.add(node);
        if(adjs.length == 0) {res[node] = true; return true;}
        for(int adj : adjs){
            if(!dfs(adj,visited,graph,res)) return false;
        }
        res[node] = true;
        return true;
    }
}

/*
st: 12:15

sub: 12:39
    -> wrong ans 
*/