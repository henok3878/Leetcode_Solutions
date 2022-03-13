class Solution {
    public int tribonacci(int n) {
        if(n == 0) return 0;
        else if(n == 1 || n == 2 ) return 1; // base case 
        
        int[] dp = new int[n + 1];
        dp[1] = 1; dp[2] = 1; // base case 
        
        for(int i = 3; i <= n; i++) // i represents state 
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]; // recurence relation 
        
        return dp[n];
    }
}