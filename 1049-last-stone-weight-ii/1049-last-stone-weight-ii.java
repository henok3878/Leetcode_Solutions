class Solution {
    public int lastStoneWeightII(int[] stones) {
        if(stones == null || stones.length == 0) return 0;
        
        int sum = Arrays.stream(stones).sum(), half_sum = sum/2;
        
        int dp[] = new int[half_sum + 1];
        for(int i=0; i<stones.length; i++) {
            for(int w=half_sum; w>=stones[i]; w--) {
                dp[w] = Math.max(dp[w], dp[w-stones[i]] + stones[i]);
            }
        }

        return sum - 2 * dp[half_sum];
    }
}