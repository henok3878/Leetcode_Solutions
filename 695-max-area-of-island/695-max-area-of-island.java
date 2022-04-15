class Solution {
    int[][] dirs = {{0,0},{1,0},{-1,0},{0,1},{0,-1}}; 
    public int maxAreaOfIsland(int[][] grid) {
        
        int ans = 0;
        int m = grid.length, n = grid[0].length;
        UnionFind uf  = new UnionFind(m,n);
        for(int i = 0;i < m; i++){
            for(int j = 0;j < n;j ++){
                for(int[] dir : dirs){
                    int x = i + dir[0], y = j + dir[1];
                    if(grid[i][j] == 1 && isInBound(x,y,m,n) && grid[x][y] == 1){
                        ans = Math.max(ans,uf.union(i*n + j, x*n + y));  
                    }
                }
            }
        }        
        return ans;
    }
    
    private boolean isInBound(int i, int j, int r, int c){
        if(i < 0 || j < 0 || i >= r || j >= c)
            return false;
        else return true;
    }
}

public class UnionFind{
    
    int[] parents;
    int[] sizes;
    
    public UnionFind(int m, int n){
        parents = new int[m*n];
        sizes = new int[m*n];
        for(int i = 0; i < m*n; i++){
            parents[i] = i;
            sizes[i] = 1;
        }
    }
    
    public int find(int el){
        if(parents[el] == el) 
            return el;
        return parents[el] = find(parents[el]);
    }
    
    public int union(int el1, int el2){
        int p1 = find(el1);
        int p2 = find(el2);
        
        if(p1 == p2) 
            return sizes[p1];
        if(sizes[p1] > sizes[p2]){
            parents[p2] = p1;
            return sizes[p1] += sizes[p2];
            
        }else{
            parents[p1] = p2;
            return sizes[p2] += sizes[p1];
        }
    }
    
    
}