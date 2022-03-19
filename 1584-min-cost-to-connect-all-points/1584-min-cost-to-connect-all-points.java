class Solution {
    public int minCostConnectPoints(int[][] points) {
        int numOfPts = points.length;
        
        List<Edge> edges = new ArrayList<>();
        
        for(int i = 0; i < numOfPts; i++){
            for(int j = i + 1;j < numOfPts; j++){
                int[] pt1 = points[i]; 
                int[] pt2 = points[j];
                int cost = Math.abs(pt1[0] - pt2[0])  + Math.abs(pt1[1] - pt2[1]);
                edges.add(new Edge(i,j,cost));
            }
        }
        
        Collections.sort(edges, (a,b)-> a.cost - b.cost); // increasing based on cost 
        
        int totalCost = 0;
        int edgesUsed = 0;
        UnionFind uf = new UnionFind(numOfPts);

        for(int i = 0; i < edges.size() && (edgesUsed < (numOfPts - 1)); i++){
            Edge edge = edges.get(i);
            if(uf.union(edge.stPtIdx, edge.endPtIdx)){
                edgesUsed++;
                totalCost += edge.cost;
            }
        }
        
        return totalCost;
        
        
    }
}
class UnionFind{
    
    int[] parents;
    int[] ranks;
    
    public UnionFind(int size){
        parents = new int[size];
        for(int i = 0; i < size; i++) parents[i] = i;
        ranks = new int[size];
    }
    
    public int find(int elem){
        if(parents[elem] == elem) return elem;
        return parents[elem] = find(parents[elem]); // path compression 
    }
    
    public boolean union(int elem1, int elem2){
        int parent1 = find(elem1);
        int parent2 = find(elem2);
        
        if(parent1 == parent2) return false; // cycle 
        
        if(ranks[parent1] > ranks[parent2])
            parents[parent2] = parent1;
        else if(ranks[parent1] < ranks[parent2])
            parents[parent1] = parent2;
        else {
            parents[parent2] = parent1;
            ranks[parent1]++;
        }
        
        return true;
    }
    
    
}


class Edge{
    int stPtIdx;
    int endPtIdx;
    int cost;
    
    public Edge(int st, int end, int cost){
        stPtIdx = st;
        endPtIdx = end;
        this.cost = cost;
    }
    
    public String toString(){
        return "(" + stPtIdx + "," + endPtIdx + ","+ cost + ")" ;
    }
    
}

/*

*/