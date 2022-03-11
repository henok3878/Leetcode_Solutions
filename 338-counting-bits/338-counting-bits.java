class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n+1];
        
        for(int i = 0; i <= n; i++) ans[i] = helper(i);
        
        return ans;
    }
    
    private int helper(int n){
        if(n == 0) return 0;
        else if(n == 1) return 1;
        
        return (n %2 == 0) ? helper(n/2) : 1 + helper(n/2);
    }
}

/*

*/