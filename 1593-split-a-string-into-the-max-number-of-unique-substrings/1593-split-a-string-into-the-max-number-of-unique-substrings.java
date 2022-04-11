class Solution {
    public int maxUniqueSplit(String s) {
        Set<String> set = new HashSet<>();
        return helper(s,0,set);
    }
    
    private int helper(String s, int st, Set<String> visited){
        //System.out.println(s.substring(st));
        if(st >= s.length())
            return 0;
        int res = 0;
        for(int end = st + 1; end <= s.length(); end++){
            //choose 
            String str = s.substring(st,end);
            if(visited.contains(str))
                continue;
            visited.add(str);
            // explore 
            res = Math.max(res,1 + helper(s,end,visited));
            visited.remove(str);
            // unchoose
        }
       
        return res;
    }
    
}

/*
Input: s = "a b a b c c c"
            0 1 2 3 4 5 6
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.

a,babcc
ab,abcc

*/