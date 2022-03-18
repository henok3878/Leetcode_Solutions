class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        
        UnionFind uf = new UnionFind(edges.length);
        
        for(int[] edge : edges){
            int node1 = edge[0], node2 = edge[1];
            if(uf.union(node1,node2) == 0) return edge;
        }
        
        return new int[]{0,0};
    }
}

class UnionFind{
    int[] root;
    int[] rank;
        
    public UnionFind(int size){
        root = new int[size + 1];
        rank = new int[size + 1];
        for(int i = 0; i <= size; i++) root[i] = i;
    }
    
    public int find(int elem){
        
        if(root[elem] == elem) return elem;
        
        return root[elem] = find(root[elem]); // with path compression 
    }
    
    public int union(int elem1, int elem2){
        
        int root1 = find(elem1);
        int root2 = find(elem2);
        
        if(root1 == root2) return 0;
        
        // union by rank
        if(rank[root1] > rank[root2]){
            root[root2] = root1;
        }
        else if(rank[root1] < rank[root2]){
            root[root1] = root2;
        }
        else{
            root[root2] = root1;
            rank[root1]++;
        }
        
        return 1;
        
        
    }
    
    
}