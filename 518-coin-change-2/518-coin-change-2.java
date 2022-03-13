class Solution {
    public int change(int amount, int[] coins) {        
        
        int[] ways = new int[amount+1]; ways[0] = 1;
        
        for(int c : coins){
          for(int i = 1; i <= amount; i++){
              int comp = (i - c < 0) ? 0 : ways[i-c];
              ways[i] += comp;
          } 
        }
        
        return ways[amount];
    }
}

/*
coins = [1,2,5] 
amt: 5
    - 1 + 1 + 1 + 1 + 1
    - 1 + 1 + 1 + 2
    - 1 + 2 + 2 
    - 5


*/