class Solution {
    
    int[] colors;
    List<List<Integer>> graph;
    public boolean possibleBipartition(int n, int[][] dislikes) {
        colors  = new int[n + 1];
        colors[0] = -1;
        graph = new ArrayList<>();
        for(int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for(int[] edge : dislikes){
            int u = edge[0], v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        
        for(int i = 1; i <= n; i++){
            if(colors[i] == 0 && !dfs(i,0)) return false;
        }
        
        return true;
    }
    
    private boolean dfs(int n, int p){
        if(colors[n]  != 0 && colors[n] == colors[p]) return false;
        else if(colors[n] != 0 && colors[n] != colors[p]) return true;
        colors[n] = -1 * colors[p];
        
        for(int adj : graph.get(n)){
            if(!dfs(adj,n)) return false;
        }
        return true;
    }
}

/*
st: 3:48 

testing: 4:18

sub: 4:23 
    - failed 
    
break: 4:47 
    
    n -> rep num of peoples 
    dislikes[i] = [ai,bi] -> person with name ai doesn't like the person called bi

st from scratch: 7:50

test: 8:05 

*/