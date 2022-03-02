class Solution {
    public int nthUglyNumber(int n) {
       Queue<Long> pq = new PriorityQueue<>();
       Set<Long> visited = new HashSet<>();
       pq.add((long)1);
       Long res = (long)1;
       for(int i = 0; i < n; i++){
            res = pq.poll();
            long twos = res*2;
            long threes = res*3;
           long fives = res*5;
            if(!visited.contains(twos)){
                pq.add(twos);
                visited.add(twos);
            }
            if(!visited.contains(threes)) {
                pq.add(threes);
                visited.add(threes);}
            if(!visited.contains(fives)) {
                pq.add(fives);
                visited.add(fives);}
       } 
        
       return res.intValue();
	}
}