class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> counts = new HashMap<>();
        for(int num : nums){
            int freq = counts.getOrDefault(num, 0) + 1;
            counts.put(num,freq);
        }
        Queue<Elem> pq = new PriorityQueue<Elem>((a,b)-> a.freq - b.freq);
        for(Map.Entry<Integer,Integer> entry : counts.entrySet()){
            int num = entry.getKey();
            int freq = entry.getValue();
            pq.add(new Elem(freq,num));
            if(pq.size() > k) pq.poll();
        }
        
        int[] ans = new int[k];
        int idx = 0;
        while(!pq.isEmpty()){
            ans[idx] = pq.poll().num;
            idx++;
        }
        
        return ans;
        
    }
}

class Elem{
    int freq;
    int num;
    
    Elem(int freq, int num){
        this.freq = freq;
        this.num = num;
    }
}
/*
    st: 9:15
    1st Test: 9:22
    
    
    [1,2,2,3] k = 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    

*/