class Solution {
    public int numSimilarGroups(String[] strs) {
        int n = strs.length;
        int components = n;
        UnionFind uf = new UnionFind(n);
        
        for(int i = 0; i < n; i++){
            for(int j = i + 1;j < n; j++){
                if(isSimilar(strs[i],strs[j]))
                    components -= uf.union(i,j);
            }
        }
        
        return components;
    }
    
    
    private boolean isSimilar(String s1, String s2){
        int count = 0;
        for(int i = 0; i < s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i) && ++count > 2) return false;
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
    
    public int union(int elem1, int elem2){
        int parent1 = find(elem1);
        int parent2 = find(elem2);
        
        if(parent1 == parent2) return 0;
        
        if(ranks[parent1] > ranks[parent2])
            parents[parent2] = parent1;
        else if(ranks[parent1] < ranks[parent2])
            parents[parent1] = parent2;
        else{
            parents[parent2] = parent1;
            ranks[parent1]++;
        }
        return 1;
    }
}