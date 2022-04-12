class Solution {
    public int maxUniqueSplit(String s) {
        return helper(0,s,new HashSet<>());
    }
    
    private int helper(int idx,String s, Set<String> v){
        if(idx >= s.length())
            return 0;
        
        int res = Integer.MIN_VALUE;
        // for loop simulate decision spaces
        for(int end = idx + 1; end <= s.length(); end++){
            
            String sub = s.substring(idx,end);
            
            // constraint 
            if(!v.contains(sub)){
                v.add(sub);
                res = Math.max(res, 1 + helper(end,s,v));
                v.remove(sub);
            }
        }
        
        return res;
    }
}

/*
goal: reach the end while satsfiying constraints 
constriant: non-empty, unique 

state: index


*/