class Solution {
    
    Integer[][] dp;
    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        dp = new Integer[n][n];
        
        int[] prefixSum = new int[n+1];
        for(int i = 1; i <= n; i++) prefixSum[i] = prefixSum[i-1] + stoneValue[i-1];
        
        return simulate(0,n-1,prefixSum,dp);
    }
    
    private int simulate(int left, int right,int[] prefixSum,Integer[][] dp ){
        
        if(left == right) return 0;
        if(dp[left][right] != null) return dp[left][right];
        
        int ans = Integer.MIN_VALUE;
        for(int i = left + 1; i <= right; i++){
            int lSum = prefixSum[i]-prefixSum[left];
            int rSum = prefixSum[right+1] - prefixSum[i];
            
            if(lSum < rSum){
                ans = Math.max(ans,lSum + simulate(left,i-1,prefixSum,dp));
            }else if(lSum > rSum){
                ans = Math.max(ans,rSum + simulate(i,right,prefixSum,dp));
            }else{
                 ans = Math.max(ans,Math.max(lSum + simulate(left,i-1,prefixSum,dp),rSum + simulate(i,right,prefixSum,dp)));
            }
        }
        
        return dp[left][right] = ans;
        
    }
}

/*
 [6,2,3,4,5,5]
 
 
 [0,6,8,11,15,20,25



*/