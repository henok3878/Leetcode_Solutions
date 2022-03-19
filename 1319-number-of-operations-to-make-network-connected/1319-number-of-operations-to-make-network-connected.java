class Solution {
    public int makeConnected(int n, int[][] connections) {
        int cabels = connections.length;
        if(cabels < n - 1) return -1;
        
        UnionFind uf = new UnionFind(n);
        
        for(int[] connection : connections){
            n -= uf.union(connection[0],connection[1]);
        }
        return n - 1;
        
    }
}

class UnionFind{
    
    int[] parents;
    int[] ranks;
    
    public UnionFind(int size){
        parents = new int[size];
        ranks = new int[size];
        for(int i = 0; i < size; i++) parents[i] = i;
    }
    
    public int find(int elem){
        if(parents[elem] == elem) return elem;
        
        return parents[elem] = find(parents[elem]); // with path compression 
    }
    
    public int union(int elem1, int elem2){
        int parent1 = find(elem1);
        int parent2 = find(elem2);
        
        if(parent1 == parent2) return 0;
        
        if(ranks[parent1] > ranks[parent2]){
            parents[parent2] = parent1;
        }
        else if(ranks[parent1] < ranks[parent2]){
            parents[parent1] = parent2;
        }else{
            parents[parent2] = parent1;
            ranks[parent1]++;
        }
        
        return 1;
    }
    
    
}