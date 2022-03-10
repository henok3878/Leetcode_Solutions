class Solution {
    public int maxProfit(int[] prices) {
        
        if(prices==null || prices.length<=1)return 0;
        
        int n=prices.length;
        int[] p = new int[n];
        int cash = 0; 
        
        p[0]=0; 
        cash = -prices[0]; 
        p[1]= Math.max(0, prices[1]-prices[0]);
        cash = Math.max(cash,-prices[1]);
        
        for(int i=2;i<n;i++){
    
            p[i] = Math.max(p[i-1], cash+prices[i]);

            cash = Math.max(cash, p[i-2]-prices[i]);
        }
        
        return p[n-1];        
        
    }
}