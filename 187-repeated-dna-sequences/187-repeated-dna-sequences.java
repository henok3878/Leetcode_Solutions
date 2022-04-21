class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        
        int size = 10;
        int n = s.length(); 
        
        Set<String> visited = new HashSet<>();
        Set<String> ans = new HashSet<>();
        
        for(int i = 0;i <= n - size; i++){
            String str = s.substring(i, i + size);
            if(visited.contains(str))
                ans.add(str);
            else
                visited.add(str);
        }
        
        return new ArrayList<>(ans);
    }
}