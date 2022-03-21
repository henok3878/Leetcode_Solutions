class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        Map<Integer,List<Integer>> graph = new HashMap<>();
        for(int i = 0;i < n; i++) graph.put(i, new ArrayList<>());
        int[] indegree = new int[n];
        
        for(int[] edge : edges){
            indegree[edge[1]]++;
            graph.get(edge[0]).add(edge[1]);
        }
        
        Queue<Integer> queue = new LinkedList<>();
        
        for(int i = 0; i < n; i++){
            if(indegree[i] == 0) queue.add(i);
        }
        Map<Integer,Set<Integer>> ancestor = new HashMap<>();
        for(int i = 0;i < n; i++) ancestor.put(i, new HashSet<>());

        
        while(!queue.isEmpty()){
            
            int curr = queue.poll();
            
            for(int adj : graph.get(curr)){
                ancestor.get(adj).add(curr);
                ancestor.get(adj).addAll(ancestor.get(curr));
                if(--indegree[adj] == 0) queue.add(adj);
            }
            
        }
        List<List<Integer>> ans = new ArrayList<>();
        for(int i = 0; i < n; i++){
            List<Integer> curr = new ArrayList<>(ancestor.get(i));
            Collections.sort(curr);
            ans.add(curr);
        }
        
        return ans;
        
    }
}