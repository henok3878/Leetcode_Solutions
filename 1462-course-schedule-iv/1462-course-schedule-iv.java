class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
       
        Map<Integer,List<Integer>> graph = new HashMap<>();
        for(int i = 0; i < numCourses; i++) graph.put(i, new ArrayList<>());
        
        for(int[] pair : prerequisites){
            graph.get(pair[0]).add(pair[1]);
        }
        
        Map<Integer,Set<Integer>> preqs = new HashMap<>();
        
        for(int c = 0; c < numCourses; c++){
            if(preqs.get(c) == null){
                dfs(c,preqs,graph);
            }
        }
        
        List<Boolean> ans = new ArrayList<>();

        for(int[] query: queries){
            Set<Integer> nextCourses = preqs.get(query[0]);
            if(nextCourses != null && nextCourses.contains(query[1]))
                ans.add(true);
            else ans.add(false);
        }
        
        return ans;
    }
    
    private Set<Integer> dfs(int c, Map<Integer,Set<Integer>> preqs, Map<Integer,List<Integer>> graph){
        
        if(preqs.get(c) != null) return preqs.get(c);
        
        Set<Integer> set = new HashSet<>();
        List<Integer> adjs = graph.get(c);
        if(adjs.size() == 0) return set;
        
        for(int adj : adjs){
            set.add(adj);
            set.addAll(dfs(adj,preqs,graph));
        }
        
        preqs.put(c,set);
        return set;
        
    }
}