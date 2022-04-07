class Solution {
    public int lastStoneWeight(int[] stones) {
        
        Queue<Integer> pq = new PriorityQueue<Integer>((a,b) -> b - a);
        for(int s : stones) pq.add(s);
        
        while(pq.size() > 1){
            int f = pq.poll();
            int s = pq.poll();
            if(f > s) pq.add(f - s);
        }
        
        return (pq.isEmpty()) ? 0 : pq.poll();
    }
}