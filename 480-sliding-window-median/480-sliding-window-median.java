class Solution {
    Queue<Integer> minHeap;
    Queue<Integer> maxHeap;
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        double[] ans = new double[n - k + 1];
        minHeap = new PriorityQueue<>((a,b)->Integer.compare(b,a));
        maxHeap = new PriorityQueue<>();
        
        for(int i = 0; i < k; i++){
            add(nums[i]);
        } // first window is done;
        ans[0] = findMedian();

        for(int i = 1; i < ans.length; i++){
            int prev = i - 1;
            if(nums[prev] != nums[prev+k]){
                remove(nums[prev]);
                add(nums[prev+k]);
            }
            //System.out.println(minHeap + " : " + maxHeap);

            ans[i] = findMedian();
        }
        
        
        
        return ans;
    }
    
    
    private void add(int elem){
        if(!minHeap.isEmpty() && minHeap.peek() >= elem){
            minHeap.add(elem);
        }else if(!maxHeap.isEmpty() && maxHeap.peek() < elem) maxHeap.add(elem);
        else minHeap.add(elem);
        balance();
    }
    
    private void remove(int elem){
        if(minHeap.peek() >= elem){
            minHeap.remove(elem);
        }else maxHeap.remove(elem);
        balance();
    }
    
    private double findMedian(){
        if(minHeap.size() == maxHeap.size()) return ((long)minHeap.peek() + maxHeap.peek())/2.0;
        else return (minHeap.size() > maxHeap.size()) ? minHeap.peek() : maxHeap.peek();
    }
    
    private void balance(){
        if(minHeap.size() > maxHeap.size() + 1){
            maxHeap.add(minHeap.poll());
        }
        else if(maxHeap.size() > minHeap.size() + 1){
            minHeap.add(maxHeap.poll());
        }
    }
}