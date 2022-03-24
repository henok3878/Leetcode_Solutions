class Solution {
    public int numSimilarGroups(String[] strs) {
                     
        Set<String> visited = new HashSet<>();
        int groups = 0;
        for(String s : strs){
            if(!visited.contains(s)){
                dfs(s,visited,strs);
                groups++;
            }
        }
        
        return groups;
        
        
    }
    
    private void dfs(String s, Set<String> visited, String[] strings){
        if(visited.contains(s)) return;
        visited.add(s);
        for(String adj : strings){
            if(isSimilar(s,adj))
                dfs(adj,visited,strings);
        }
    }
    
    
    private boolean isSimilar(String s1, String s2){
        int count = 0;
        for(int i = 0; i < s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i) && ++count > 2) return false;
        }
        return true;
    }
}
