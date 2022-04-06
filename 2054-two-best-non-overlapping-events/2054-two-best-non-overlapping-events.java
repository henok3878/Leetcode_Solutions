class Solution {
    public int maxTwoEvents(int[][] events) {
        
        Arrays.sort(events,(a,b)->(a[0] == b[0]) ? a[1] - b[1] : a[0] - b[0]);
        
        Integer[][] dp = new Integer[events.length][3];
        
        return helper(0,0,events,2,dp);
      
    }
    
    private int helper(int idx, int end, int[][] events,int attended, Integer[][] dp){
        if(idx >= events.length || attended <= 0) return 0;
        
        if(dp[idx][attended] != null) return dp[idx][attended];
        
        int[] evt = events[idx];
        
        int nxt = findNxt(events,idx);
        int take = evt[2] + helper(nxt,evt[1],events, attended - 1,dp);
        int skip = helper(idx+1,end,events, attended,dp);
        return dp[idx][attended] = Math.max(take,skip);
        
    }
    
    private int findNxt(int[][] evts, int idx){
        int st = idx;
        int end = evts.length - 1;
        while(st <= end){
            int mid = st + (end - st)/2;
            if(evts[mid][0] > evts[idx][1]){
                end = mid - 1;
            }else st = mid + 1;
        }
        return st;
    }
}
