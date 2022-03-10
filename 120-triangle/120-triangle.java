class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int levels = triangle.size();
        int lastRow = triangle.get(levels-1).size();
        int[][] dp = new int[levels][lastRow + 1];
        for(int[] row : dp) Arrays.fill(row, Integer.MAX_VALUE);
        dp[0][1] = triangle.get(0).get(0);
        
        for(int i = 1;i < levels; i++){
            for(int j = 1; j <= i + 1;j++){
                dp[i][j] = triangle.get(i).get(j-1) + Math.min(dp[i-1][j], dp[i-1][j-1]);
            }
        }
        
        int ans = Integer.MAX_VALUE;
        for(int num : dp[levels-1]) ans = Math.min(ans,num);
        
        return ans;
    }
}