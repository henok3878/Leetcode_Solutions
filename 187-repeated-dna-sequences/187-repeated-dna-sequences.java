class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        
        int size = 10;
        int n = s.length(); 
        if(n <= size)
            return new ArrayList<>();
        
        Set<String> visited = new HashSet<>();
        Set<String> ans = new HashSet<>();
        
        StringBuilder sb = new StringBuilder(s.substring(0,size));
        for(int i = 0;i <= n - size; i++){
            if(i > 0){
                sb.deleteCharAt(0);
                sb.append(s.charAt(i + size - 1));
            }
            String str = sb.toString();
            if(visited.contains(str))
                ans.add(str);
            else
                visited.add(str);
        }
        
        return new ArrayList<>(ans);
    }
}