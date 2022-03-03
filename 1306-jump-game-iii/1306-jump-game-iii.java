class Solution {
    public boolean canReach(int[] arr, int start) {
        int size = arr.length;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        
        while(!queue.isEmpty()){
            Integer curr = queue.poll();
            if(arr[curr] == 0) return true;
            int left = curr - arr[curr], right = curr + arr[curr];
            if(left >= 0 && arr[left] >= 0)
                queue.add(left);
            if(right < size && arr[right] >= 0) queue.add(right);
            arr[curr] *= -1;
        }
        return false;
    }
}

/*
    st: 2 : 28
    
    end: 2:43 

*/