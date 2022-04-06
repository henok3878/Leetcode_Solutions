class Solution {
    public int minCost(int n, int[] cuts) {
        int m = cuts.length;
        int[] newCuts = new int[m + 2];
        for(int i = 0; i <m ; i++) newCuts[i+1] = cuts[i];
        newCuts[0] = 0;
        newCuts[m+1] = n;
        Arrays.sort(newCuts);
        Integer[][] dp = new Integer[m+2][m+2];
        
        return helper(0,m+1,newCuts,dp);
    }
    
    private int helper(int left, int right, int[] cuts, Integer[][] dp){
        //System.out.println("l: " + left + " r: " + right);
        if(dp[left][right] != null)
            return dp[left][right];
        else if(right - left == 1) 
            return dp[left][right] = 0;
        
        int cost = Integer.MAX_VALUE;
        for(int i = left + 1; i < right; i++)
            cost = Math.min(cost,helper(left,i,cuts,dp) + helper(i,right,cuts,dp));
        
        return dp[left][right] = (cuts[right] - cuts[left]) + cost;
    }
}

