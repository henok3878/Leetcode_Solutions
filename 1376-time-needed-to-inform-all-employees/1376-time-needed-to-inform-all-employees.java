class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        
        
        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0; i < n; i++) graph.add(new ArrayList<>());
        for(int i = 0; i < n; i++){
            if(i == headID) continue;
            graph.get(manager[i]).add(i);
        }
        int time = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(headID);
        
        while(!queue.isEmpty()){
            
            int curr = queue.poll();
            int manag = manager[curr];
            informTime[curr] +=  (manag == -1 ) ? 0 : informTime[manag];
            time = Math.max(time,informTime[curr]);
            // here add adj to queue 
            for(int sub : graph.get(curr)){
                queue.add(sub);
            }
        }
        
        return time;
        
    }
}

/*
st: 9:25 

*/