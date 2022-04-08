class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
        Arrays.sort(edges,(a,b) -> b[0] - a[0]);
        
        UnionFind uf1  = new UnionFind(n + 1);
        UnionFind uf2 = new UnionFind(n + 1);
        int t3 = 0;
        int usedT2 = 0;
        int usedT1 = 0;
        for(int[] edge : edges){
            
            if(edge[0] == 3){
               if(uf1.union(edge[1],edge[2])){
                    t3++;
               }
               uf2.union(edge[1],edge[2]);
            }else if(edge[0] == 1){
                if(uf1.union(edge[1],edge[2])){
                    usedT1++;
                }
            }
            else{
                if(uf2.union(edge[1],edge[2]))
                    usedT2++;
            }
             
        }
        if(usedT2 + t3 == n -1 && usedT1 + t3 == n -1 )
            return edges.length - (usedT1 + usedT2 + t3);
        return -1;
    }
}

class UnionFind{
    int[] parents;
    int[] ranks;
    
    public UnionFind(int n){
        parents = new int[n];
        ranks = new int[n];
        
        for(int i = 0; i < n; i++) parents[i] = i;
    }
    
    public int find(int elem){
        if(parents[elem] == elem) return elem;
        return parents[elem] = find(parents[elem]); // path compression 
    }
    
    public boolean union(int e1, int e2){
        int p1 = find(e1);
        int p2 = find(e2);
        if(p1 == p2) 
            return false;
        if(ranks[p1] > ranks[p2])
            parents[p2] = p1;
        else if(ranks[p1] < ranks[p2])
            parents[p1] = p2;
        else{
            parents[p1] = p2;
            ranks[p2]++;
        }
        return true;
    }
}