class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String,Integer> counts = new HashMap<>();
        for(String word : words){
            int freq = counts.getOrDefault(word,0) + 1;
            counts.put(word,freq);
        }
        
        Queue<Word> pq = new PriorityQueue<Word>((a,b)->(a.freq == b.freq) ? b.word.compareTo(a.word) : a.freq - b.freq);
        
        for(Map.Entry<String,Integer> entry : counts.entrySet()){
            String word = entry.getKey();
            int freq = entry.getValue();
            pq.add(new Word(word,freq));
            if(pq.size() > k) pq.poll();
        }
                
        List<String> ans = new ArrayList<>();
        
        while(!pq.isEmpty()) ans.add(0,pq.poll().word);
            
        return ans;
        
        
    }
}


class Word {
    
    int freq;
    String word;
    public Word(String word, int freq){
        this.freq = freq;
        this.word = word;
    }
    
}

/*

st time: 9:25 

end time: 9:55

*/