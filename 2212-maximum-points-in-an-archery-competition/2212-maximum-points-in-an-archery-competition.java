class Solution {
    
    int max = Integer.MIN_VALUE;
    int[] ans = new int[12];
    public int[] maximumBobPoints(int numArrows, int[] aliceArrows) {
        int[] selected = new int[12];
        
        dfs(0,0,0,selected,numArrows,aliceArrows); // i, used, sum so far,selected ...
        
        return ans;
        
    }
    
    private void dfs(int i,int used, int currSum,int[] selected,int n, int[] alice){
        if(i >= selected.length){
            if(used <= n && currSum > max){
                max = currSum;
                for(int s = 0; s < 12; s++) ans[s] = selected[s];
                if(used < n) ans[0] += n - used;
            }
            return;
        }
        else if(used > n) return;
        
       
        selected[i]=alice[i] + 1;
        dfs(i+1, used + alice[i] + 1, currSum + i,selected,n,alice);
        selected[i] = 0;
        dfs(i+1,used,currSum,selected,n,alice); // not selected 
    }
}

/*
both shoots = n times 



*/