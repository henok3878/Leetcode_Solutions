class Solution {
    
    Queue<Integer> minHeap = new PriorityQueue<>();
    Queue<Integer> maxHeap = new PriorityQueue<>((a,b) -> Integer.compare(b,a));
    
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        double[] ans = new double[n - k + 1];
        
        for(int i = 0; i < k; i++){
            add(nums[i]);
        }
        ans[0] = findMedian(k);
        remove(nums[0]);

        for(int i = 1; i <= n - k ; i++){
            add(nums[i + k - 1]);
            ans[i] = findMedian(k);
            remove(nums[i]);
        }
        
        return ans;
        
    }
    
    private void remove(int elem){
        if(!maxHeap.isEmpty() && elem <= maxHeap.peek()) maxHeap.remove(elem);
        else minHeap.remove(elem);
        balance();
    }
    private void add(int elem){

        if((!minHeap.isEmpty()) && elem < minHeap.peek()) maxHeap.add(elem);
        else if(!maxHeap.isEmpty() && elem <= maxHeap.peek()) maxHeap.add(elem);
        else minHeap.add(elem);
        balance();
    
    }
    
    private void balance(){
        if(maxHeap.size() > minHeap.size() + 1) minHeap.add(maxHeap.poll());
        else if(minHeap.size() > maxHeap.size() + 1) maxHeap.add(minHeap.poll());
    }
    
    private double findMedian(int k){
        
        double median = (k %2 == 0) ? ((double)maxHeap.peek() + (double)minHeap.peek())/2.0 : 
                (minHeap.size() > maxHeap.size()) ? minHeap.peek() : maxHeap.peek();
        return median;
    }
    
    
}
/*
st: 2:01 

test: 2:23

*/