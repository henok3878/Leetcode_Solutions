class Solution {
    public int[][] generateMatrix(int n) {
        int[][] ans = new int[n][n];        
        helper(0,n,1,ans);
        
        return ans;
        
    }
    
    private void helper(int offset, int n,int st, int[][] grid){
        //print(grid);

        // base case 
        if(n == 0)
            return;
        else if(n == 1){
            grid[offset][offset] = st;
            return;
        }
        
        for(int j = 0;j < n; j++){
            grid[offset][j + offset] = st++;
        }
        for(int i = 1; i < n; i++){
            grid[i+offset][(n-1) + offset] = st++;
        }
        for(int j = (n-2); j >= 0; j--){
            grid[(n-1) + offset][j + offset] = st++;
        }
        for(int i = (n-2); i > 0; i--){
            grid[i + offset][offset] = st++;
        }
        
        helper(offset+1,n - 2, st, grid);
    }
    private void print(int[][] g){
        for(int [] r : g){
            System.out.println(Arrays.toString(r));
        }
    }
}