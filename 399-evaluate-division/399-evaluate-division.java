class Solution {
    Map<String,List<Node>> graph;
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
       graph = new HashMap<>();
       
        for(int i = 0; i < equations.size(); i++){
            List<String> edge = equations.get(i);
            String u = edge.get(0), v = edge.get(1);
            double weight = values[i];
            List<Node> uAdj = graph.getOrDefault(u,new ArrayList<Node>());
            uAdj.add(new Node(v,weight));
            List<Node> vAdj = graph.getOrDefault(v,new ArrayList<Node>());
            vAdj.add(new Node(u,1/weight));
            
            graph.put(u,uAdj);
            graph.put(v,vAdj);
        }
        
        double[] ans = new double[queries.size()];
        
        
        for(int i = 0; i < queries.size(); i++){
            List<String> query = queries.get(i);
            String u = query.get(0), v = query.get(1);
            if(graph.containsKey(u) && graph.containsKey(v))
                ans[i] = dfs(u,v,1,new HashSet<String>());
            else ans[i] = -1;
        }
        //System.out.println(graph);
        return ans;
        
    }
    
    private double dfs(String u , String v, double weight, Set<String> visited){
        //System.out.println("u: " + u + " v: "+v + " w: " + weight + " vis: " + visited);
        if(u.equals(v)) return weight;
        visited.add(u);
        double w = -1.0;
        List<Node> adjs = graph.get(u);
        if(adjs != null){
            for(Node adj : adjs){
                if(visited.contains(adj.val)) continue;
                visited.add(adj.val);
                w = dfs(adj.val,v,weight*adj.weight,visited);
                if(w != -1) return w;
            }
        }
        return -1;
    }
}

class Node{
    String val;
    double weight; 
    
    public Node(String val, double weight){
        this.val = val;
        this.weight = weight;
    }
    
    public String toString(){
        return "(" + val + "," + weight +")";
    }
}

/*
st: 2:50 PM 

sub: 3:42


*/