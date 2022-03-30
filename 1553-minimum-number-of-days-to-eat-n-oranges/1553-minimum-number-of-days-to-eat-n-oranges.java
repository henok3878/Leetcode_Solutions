class Solution {
    public int minDays(int n) {
        
        Set<Integer> visited = new HashSet<>();
        
        Queue<Integer> q = new LinkedList<>();
        q.add(n);
        visited.add(n);
        int min = 0;
        
        while(!q.isEmpty()){
            int s = q.size();
            for(int i = 0; i < s ;i++){
                int curr = q.poll();
                if(curr == 0) return min;
                if(curr % 2 == 0 && !visited.contains(curr/2)){
                    visited.add(curr/2);
                    q.add(curr/2);
                }
                int t = curr - (2*(curr/3));
                if(curr % 3 == 0 && !visited.contains(t)){
                    visited.add(t);
                    q.add(t);
                }
                if(!visited.contains(curr - 1))
                {q.add(curr-1); visited.add(curr-1);}
            }
            min++;
            
        }
        return min;
    }
}