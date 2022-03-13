class Solution {
    public int change(int amount, int[] coins) {        
        
        int[] ways = new int[amount+1]; ways[0] = 1;
        
        for(int c : coins)
          for(int i = 1; i <= amount; i++)
              if (i - c >= 0) ways[i] +=  ways[i-c];
          
        return ways[amount];
    }
}
