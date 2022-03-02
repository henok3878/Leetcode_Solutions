class Solution {
    public int nthUglyNumber(int n) {
        PriorityQueue<Long> pq=new PriorityQueue<>();
        HashMap<Long, Boolean> map=new HashMap<>();
        int[] primes = new int[]{2,3,5};
        pq.add((long)1);
        map.put((long)1, true);
        long res=0;
        
        while(n > 0){
            res = pq.poll();
            for(int prime: primes){
                Long nextUgly = res* prime;
                if(!map.containsKey(nextUgly)){
                    pq.add(nextUgly);
                    map.put(nextUgly, true);
                }
            }
            n--;
        }      
        return (int) res;
	}
}