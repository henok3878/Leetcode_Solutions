class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        UnionFind uf = new UnionFind(n);
        
        for(int i = 0;i < n; i++){
            
            for(int j = 0;j < graph[i].length; j++){
                
                if(uf.isConnected(i,graph[i][j])) return false;
                uf.union(graph[i][0], graph[i][j]);
            }
        }
        return true;
    }
}

class UnionFind{
    
    int[] parents;
    int[] ranks;
    
    public UnionFind(int size){
        parents = new int[size];
        ranks = new int[size];
        for(int i = 0;i < size; i++) parents[i] = i;
    }
    
    public int find(int elem){
        if(parents[elem] == elem) return elem;
        return parents[elem] = find(parents[elem]);
    }
    
    public void union(int elem1, int elem2){
        int parent1 = find(elem1);
        int parent2 = find(elem2);
        
        if(parent1 == parent2) return;
        if(ranks[parent1] > ranks[parent2])
            parents[parent2] = parent1;
        else if(ranks[parent1] < ranks[parent2])
            parents[parent1] = parent2;
        else{
            parents[parent2] = parent1;
            ranks[parent1]++;
        }
    }
    
    public boolean isConnected(int elem1, int elem2){
        return find(elem1) == find(elem2);
    }

}

