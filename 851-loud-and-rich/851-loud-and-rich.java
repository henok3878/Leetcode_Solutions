class Solution {
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        
        int n = quiet.length;// num of people
        Map<Integer,List<Integer>> graph = new HashMap<>();
        for(int i = 0; i < n; i++) graph.put(i,new ArrayList<>());
        
        for(int[] pair : richer){
            int u = pair[1], v = pair[0]; // u -> v
            graph.get(u).add(v);
        }
        
        //System.out.println(graph);
        
        int[] ans = new int[n];
        Arrays.fill(ans,-1);
        
        for(int p = 0; p < n; p++){
            if(ans[p] == -1){
                dfs(p,ans,quiet,graph);
            }
        }
             
        return ans;
    }
    
    private int dfs(int pers, int[] ans,int[] quiet, Map<Integer,List<Integer>> graph){
        if(ans[pers] != -1) return ans[pers];
        
        List<Integer> adjs = graph.get(pers);
        if(adjs.size() == 0) return ans[pers] = pers;
        int q = quiet[pers], p = pers; 
        for(int adj : adjs){
            int res = dfs(adj,ans,quiet,graph);
            if(q >= quiet[res]){
                q = quiet[res];
                p = res;
            }
        }
        ans[pers] = p;
        return p;
    }
}