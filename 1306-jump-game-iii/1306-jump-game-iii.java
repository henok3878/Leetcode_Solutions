class Solution {
    public boolean canReach(int[] arr, int start) {
        int size = arr.length;
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        queue.add(start);
        visited.add(start);
        
        while(!queue.isEmpty()){
            Integer curr = queue.poll();
            if(arr[curr] == 0) return true;
            int left = curr - arr[curr], right = curr + arr[curr];
            if(left >= 0 && !visited.contains(left)){
                visited.add(left);
                queue.add(left);
            }
            if(right < size && !visited.contains(right)){
                visited.add(right);
                queue.add(right);
            }
        }
        return false;
    }
}

/*
    st: 2 : 28
    
    end: 2:43 

*/