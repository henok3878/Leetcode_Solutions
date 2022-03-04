class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        
        int n = rooms.size();
        int visits = 1;
        boolean[] visited = new boolean[n];
        
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        visited[0] = true;
        
        while(!queue.isEmpty()){
            int curr = queue.poll();
            
            for(int adj : rooms.get(curr)){
                if(visited[adj]) continue;
                queue.add(adj);
                visited[adj] = true;
                visits++;
            }
        }
        
        return visits == n;
        
        
    }
}

/*
Solution 1: Using BFS 
    st: 9:40 
    sub: 9:52 
    
Solution 2: Using DFS
    

*/