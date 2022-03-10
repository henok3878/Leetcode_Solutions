class Solution {
    public boolean divisorGame(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return helper(n,true,dp);
    }
    private boolean helper(int n, boolean turn,int[] dp){
        if(n == 2) return turn;
        else if(n < 2) return !turn;
        else if(dp[n] != -1) return (dp[n] == 1) ? turn : !turn;
        
        for(int x = 1; x < n; x++){
            if(n % x == 0 && helper(n - x,!turn,dp) == turn){
                 dp[n] = 1;
                 return turn;
            }
            
        }
        dp[n] = 0;   
        return !turn;
    }
    
}

/*
    Arrays.sort(intervals, (a,b)-> a[0] - b[0]); // increasing, based on st 
    


*/