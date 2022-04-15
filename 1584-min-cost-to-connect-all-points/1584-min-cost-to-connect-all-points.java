class Solution {
    public int minCostConnectPoints(int[][] points) {
        List<int[]> edges = new ArrayList<>();
        int pts = points.length;
        for(int i = 0;i < pts; i++){
            int[] p1 = points[i];
            for(int j = i + 1; j < pts; j++){
                int[] p2 = points[j];
                int dist = Math.abs(p2[0] - p1[0]) + Math.abs(p2[1] - p1[1]);
                edges.add(new int[]{i,j,dist});
            }
        }
        UnionFind uf = new UnionFind(pts);
        
        Collections.sort(edges,(a,b)-> a[2] - b[2]);
        int cost = 0;
        for(int[] edge : edges){
            if(uf.union(edge[0],edge[1]))
                cost += edge[2];
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
        for(int i = 0; i < n; i++)
            parents[i] = i;
    }
    
    public int find(int el){
        if(parents[el] == el) 
            return el;
        return parents[el] = find(parents[el]);
    }
    
    public boolean union(int el1, int el2){
        int p1 = find(el1);
        int p2 = find(el2);
        if(p1 == p2) 
            return false;
        if(ranks[p1] > ranks[p2])
            parents[p2] = p1;
        else if(ranks[p1] < ranks[p2])
            parents[p1] = p2;
        else{
            parents[p2] = p1;
            ranks[p2]++;
        }
        
        return true;
    }
}

/*
    Minimum spanning tree 


*/