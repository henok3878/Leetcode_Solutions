class Solution {
    int MOD = 1_000_000_007;
    public int maximumProduct(int[] nums, int k) {
        Queue<Integer> pq = new PriorityQueue<>();
        for(int n : nums) pq.add(n);
        
        long prod = 1;
        while(k-- > 0)
            pq.add(pq.poll() + 1);
        
        while(!pq.isEmpty()){
            prod *= pq.poll();
            prod %= MOD;
        }
        
        return (int)(prod);
    }
}

/*
*/