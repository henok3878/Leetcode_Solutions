class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        
        List<int[]>edges = new ArrayList<>();
        
        for(int i = 0;i < n; i++){
            int[] p1 = points[i];
            for(int j = i + 1; j < n; j++){
                int[] p2 = points[j];
                edges.add(new int[]{i,j,Math.abs(p2[0] - p1[0]) + Math.abs(p2[1] - p1[1])});
            }
        }
        
        Collections.sort(edges,(a,b)->a[2] - b[2]);
        
        UnionFind uf = new UnionFind(n);
        int cost = 0;
        
        for(int[] e : edges){
             int i = e[0], j = e[1];
             if(uf.union(i,j)) cost += e[2];
        }
        
        return cost;
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
        return parents[elem] = find(parents[elem]);
    }
    
    public boolean union(int elem1, int elem2){
        int p1 = find(elem1);
        int p2 = find(elem2);
        
        if(p1 == p2) return false;
        
        if(ranks[p1] > ranks[p2]) parents[p2] = p1;
        else if(ranks[p1] < ranks[p2]) parents[p1] = p2;
        else{
            parents[p2] = p1;
            ranks[p1]++;
        }
        
        return true;
    }
    
    
}