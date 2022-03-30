class Solution {
    public int minSwaps(int[][] grid) {
        int n = grid.length;
        int[] trailingZeros = new int[n];
        Arrays.fill(trailingZeros,n);
        
        for(int i = 0; i < n; i++){
            for(int j = 0;j < n;j ++){
                if(grid[i][j] == 1) 
                    trailingZeros[i] = n - 1 - j;
            }
        }
        
        int swaps = 0;
        
        for(int i = 0; i < n; i++){
            
            int next = -1;
            for(int j = i; j < n;j++){
                int req = n - i - 1;
                
                if(trailingZeros[j] >= req){
                    next = j;
                    break;
                }
            }
            if(next == -1) return -1;
            
            for(int j = next;j > i; j--){
                int temp = trailingZeros[j];
                trailingZeros[j] = trailingZeros[j-1];
                trailingZeros[j-1] = temp;
                swaps++;
            }
            
        } 
        return swaps;
    }
}