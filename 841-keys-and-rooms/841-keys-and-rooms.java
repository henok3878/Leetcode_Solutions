class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        
        int n = rooms.size();
        int visits = 0;
        boolean[] visited = new boolean[n];
        
        Stack<Integer> stack = new Stack<>();
        stack.add(0);
        
        while(!stack.isEmpty()){
            int curr = stack.pop();
            if(visited[curr]) continue;
            visited[curr] = true;
            visits++;
            for(int adj : rooms.get(curr)){
                if(visited[adj]) continue;
                stack.push(adj);
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
    st: 9:56 
    sub: 10:01

*/