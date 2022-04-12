class Solution {
      Map<Character,List<String>> map = new HashMap<>(){{
        put('2', new ArrayList<>(Arrays.asList("a","b","c")));
        put('3',new ArrayList<>(Arrays.asList("d","e","f")));
        put('4',new ArrayList<>(Arrays.asList("g","h","i")));
        put('5',new ArrayList<>(Arrays.asList("j","k","l")));
        put('6',new ArrayList<>(Arrays.asList("m","n","o")));
        put('7',new ArrayList<>(Arrays.asList("p","q","r","s")));
        put('8',new ArrayList<>(Arrays.asList("t","u","v")));
        put('9',new ArrayList<>(Arrays.asList("w","x","y","z")));
        }}; 
        
    
    public List<String> letterCombinations(String digits) {
        if(digits.length() == 0) return new ArrayList<>();
        List<String> ans = new ArrayList<>();
        helper(digits,0,new StringBuilder(),ans);
        return ans;
    }
    
    private void helper(String digs, int idx,StringBuilder sb, List<String> ans){
        if(idx >= digs.length()){
            ans.add(sb.toString());
            return;
        }
        // decision space for current state 
        for(String c : map.get(digs.charAt(idx))){
            // choose 
            sb.append(c);
            // explore 
            helper(digs,idx + 1,sb,ans);
            // unchoose 
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}

/*
Time Complexity: num of recurssive calls 4^N and each base case copies String to the ans which O(N)
    so total will be : O(4^N*N)

*/