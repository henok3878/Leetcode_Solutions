class Solution {
    public boolean equationsPossible(String[] equations) {
        
        UnionFind uf = new UnionFind(26);
        
        for(String eq : equations){
            String op = eq.substring(1,3);
            int x = eq.charAt(0) - 'a';
            int y = eq.charAt(3) - 'a';
            if(op.equals("=="))
                uf.union(x,y);
        }
        
       for(String eq : equations){
            String op = eq.substring(1,3);
            int x = eq.charAt(0) - 'a';
            int y = eq.charAt(3) - 'a';
            if(op.equals("!=") && uf.isConnected(x,y))
                return false;
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
        for(int i = 0; i < size; i++) parents[i] = i;
    }
    
    public int find(int elem){
        if(parents[elem] == elem) return elem;
        return parents[elem] = find(parents[elem]);
    }
    
    public boolean isConnected(int elem1, int elem2){
        return find(elem1) == find(elem2);
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
    
}