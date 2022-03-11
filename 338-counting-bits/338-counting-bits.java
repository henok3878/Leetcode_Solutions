class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n+1];
        Arrays.fill(ans,-1);
        
        for(int i = 0; i <= n; i++) ans[i] = helper(i,ans);
        
        return ans;
    }
    
    private int helper(int n,int[] ans){
        if(n == 0) return 0;
        else if(n == 1) return 1;
        else if(ans[n] != -1) return ans[n];
        
        return ans[n] = (n %2 == 0) ? helper(n/2,ans) : 1 + helper(n/2,ans);
    }
}

/*

*/