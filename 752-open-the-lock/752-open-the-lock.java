class Solution {
    public int openLock(String[] deadends, String target) {
        int level = 0; 
        Set<String> deads =  new HashSet<>();
        for(String s : deadends) deads.add(s);
        
        if(deads.contains("0000")) return -1;
        Queue<String> queue = new LinkedList<>();
        queue.add("0000");
        
        while(!queue.isEmpty()){
            //System.out.println(queue);
            int size = queue.size();
            for(int i = 0; i < size; i++){
                String curr = queue.poll();
                if(curr.equals(target)) return level;
                for(String adj : genAdj(curr)){
                    if(!deads.contains(adj)){ queue.add(adj); deads.add(adj);}
                }
                
            }
            level++;
        }        
        return -1;
        
    }
    
    private List<String> genAdj(String key){
        List<String> ans = new ArrayList<>();
        
        for(int i = 0; i < key.length(); i++){
            int curr = key.charAt(i) - '0';
            int left = (curr == 0) ? 9 : curr - 1;
            int right = (curr == 9) ? 0 : curr + 1;
            StringBuilder sb = new StringBuilder(key);
            sb.setCharAt(i,(char)(left+'0'));
            ans.add(sb.toString());
            sb.setCharAt(i,(char)(right+'0'));
            ans.add(sb.toString());
        }
        
        return ans;
    }
}

/*
st: 2:02 

test: 2:22

sub: 2:31
    **** init: 
    
    0000 => 1000, 0100, 0010, 0001, 9000, 0900, 0090, 0009
    
    0 + 1 or (0 - 1)%10  => 1 & 9
    1 -> 0 and 2 
    ....
    9 -> 8 and 0 (9+10%10)

    
*/