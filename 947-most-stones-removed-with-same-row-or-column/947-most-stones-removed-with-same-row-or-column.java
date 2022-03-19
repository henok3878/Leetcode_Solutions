class Solution {
    public int removeStones(int[][] stones) {
     
        int totalStones = stones.length;
        UnionFind uf = new UnionFind(totalStones);
        
        int ans = 0;
        
       for(int i = 0; i < totalStones; i++){
           for(int j = i +  1; j < totalStones; j++){
              int[] stone1 = stones[i];
              int[] stone2 = stones[j];
               
              if(stone1[0] == stone2[0] || stone1[1] == stone2[1])
                  ans += uf.union(i,j);
           }
       }
        
       return ans; 
        
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
        
        return parents[elem] = find(parents[elem]); // path compression 
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