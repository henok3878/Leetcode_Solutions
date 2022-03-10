class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n + 1];
        Arrays.fill(dp,-1);
        return Math.min(minCostHelper(dp,cost, n -1), minCostHelper(dp,cost, n-2));   
    }
    
    private int minCostHelper(int[] dp,int[] cost, int n){
        if(n == 1 || n == 0) return cost[n];
        else if(dp[n] != -1) return dp[n];
        int min = cost[n] + Math.min(minCostHelper(dp,cost, n -1), minCostHelper(dp,cost, n- 2));
        dp[n] = min;
        return min;
    }
}