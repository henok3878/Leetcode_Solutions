class Solution {
    public int findCircleNum(int[][] isConnected) {
        int n = isConnected.length;
        UnionFind uf = new UnionFind(n);
    
       int ans = n;
       for(int i = 0; i < n; i++){
           for(int j = 0; j < n; j++){
               if(isConnected[i][j] == 1){
                   ans -= uf.union(i,j);
               }
           }
       }
        
        return ans;
        
    }
}

class UnionFind{
    
    int[] parents;
    int[] ranks;
    
    public UnionFind(int n){
        parents = new int[n];
        ranks = new int[n];
        for(int i = 0;i < n; i++){
            parents[i] = i;
        }
    }
    
    public int find(int el){
        if(parents[el] == el) return el;
        return parents[el] = find(parents[el]);
    }
    
    public int union(int el1,int el2){
        int p1 = find(el1);
        int p2 = find(el2);
        if(p1 == p2)
            return 0;
        if(ranks[p1] > ranks[p2])
            parents[p2] = p1;
        else if(ranks[p2] > ranks[p1])
            parents[p1] = p2;
        else{
            parents[p2] = p1;
            ranks[p1]++;
        }
        
        return 1;
    }
}
/*



*/