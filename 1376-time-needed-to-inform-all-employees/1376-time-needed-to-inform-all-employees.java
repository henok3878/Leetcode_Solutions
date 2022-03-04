class Solution {
    
    List<List<Integer>> graph;
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
              
        graph = new ArrayList<>();
        for(int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for(int i = 0; i < n; i++){
            if(i == headID) continue;
            graph.get(manager[i]).add(i);
        }
        
        return dfs(headID,manager,informTime);
        
    }
    
    private int dfs(int n,int[] manager, int[] informTime){
       int manag = manager[n];
       informTime[n] +=  (manag == -1 ) ? 0 : informTime[manag];
       int res = informTime[n];
       for(int sub : graph.get(n)){
             res = Math.max(res,dfs(sub, manager,informTime));
       }
       return res;  

    }
}

/*

1st Solution: BFS 
    st: 9:25 
    sub: 9:47 
    
2nd Solution: DFS 
    st: 9:51
    sub: 9:58
*/