class Solution {
    public String reorganizeString(String s) {
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i++) count[s.charAt(i) - 'a']++;
        Queue<Letter> pq = new PriorityQueue<>((a,b) -> b.freq - a.freq);
        for(int i = 0; i < count.length; i++)
            if(count[i] > 0) pq.add(new Letter((char)(i + 'a'),count[i]));
    
        StringBuilder sb = new StringBuilder();
        
        Letter cool = null;
        while(!pq.isEmpty()){
            Letter curr = pq.poll();
            curr.freq -= 1;
            sb.append(curr.c);
            if(cool != null && cool.c != sb.charAt(sb.length() - 1)){
                pq.add(cool);
                cool = null;
            }
            if(curr.freq > 0) cool = curr; 
        }
        
        return (cool != null) ? "" : sb.toString();
    }
}
class Letter{
    char c;
    int freq;
    Letter(char c , int freq){
        this.c = c; this.freq = freq;
    }
}
/*
st: 8:46
sub: 9:19 

*/