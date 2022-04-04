class Solution {
    public long mostPoints(int[][] questions) {
        int n = questions.length;
        Long[] dp = new Long[n];
        
        return mostPointsHelper(0,questions,dp);
    }
    
    private long mostPointsHelper(int q, int[][] ques, Long[] dp){
        
        if(q >= ques.length) return 0;
        
        if(dp[q] != null) return dp[q];
        // choose current 
        long choose = ques[q][0] + mostPointsHelper(q + ques[q][1] + 1,ques,dp);
        long skip = mostPointsHelper(q+1,ques,dp);
        
        return dp[q] = Math.max(choose,skip);
        
        // skip current 
        
        
    }
}

/*
[[3,2],[4,3],[4,4],[2,5]]




*/