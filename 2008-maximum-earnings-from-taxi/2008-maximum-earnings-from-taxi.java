class Solution {
    public long maxTaxiEarnings(int n, int[][] rides) {
    
        int rLen = rides.length;
        long[] dp = new long[rLen];
        Arrays.fill(dp,-1);
        
        Arrays.sort(rides,(a,b)->a[0] - b[0]);
        
        return helper(0,rides,dp);
    }
    
    private long helper(int idx, int[][] rides,long[] dp){
        if(idx >= rides.length)
            return 0;
        else if(dp[idx] != -1){
            return dp[idx];
        }
         int next = findNext(idx,rides);
        
         long choose = (rides[idx][1] - rides[idx][0] ) + rides[idx][2] + helper(next, rides,dp);
        long skip = helper(idx + 1, rides,dp);
        
        return dp[idx] = Math.max(choose,skip);
       
    }
    
    private int findNext(int idx, int[][] rides){
        int[] curr = rides[idx];
        int st = idx, end = rides.length - 1;
        while(st <= end){
            int mid = st + (end - st ) / 2;
            if(rides[mid][0] < curr[1]){
                st = mid + 1;
            }else {
                end = mid - 1;
            }
        }
        
        return st;
    }
}

/*











    Input: n = 5, rides = [[2,5,4],[1,5,1]]
    
    First check Greedy Approach:
        -> Choices: 
            
        Greedy doesn't work here.
    
    Recursion: 
        -> choose, unchoose exploration 
        time Complxity: O(2^N)

*/