class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n]; 
        for(int i = 0; i < n; i++){
            Arrays.fill(dp[i],-1);
        }
        return helper(s,0,n -1,dp);
    }
    
    
    public int helper(String s, int i, int j, int[][] dp){
        if(dp[i][j] != -1){
            return dp[i][j];
        }
        else if( i == j){
            return 1;
        }else if (i > j){
            return 0; 
        }
        int res = 0 ;
        if(s.charAt(i) == s.charAt(j)){
            res = 2 + helper(s,i + 1, j - 1, dp);
        }
        int left = helper(s, i + 1, j, dp);
        res = Math.max(res, left);
        int right = helper(s, i , j - 1, dp);
        res = Math.max(res, right);
        
        return dp[i][j] = res;
    }
}