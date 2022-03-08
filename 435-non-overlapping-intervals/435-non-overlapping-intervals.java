class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->a[0] - b[0]);
        Stack<int[]> stack = new Stack<>();
        
        for(int[] ival : intervals){
            if(stack.isEmpty()) stack.push(ival);
            else{
                int[] top = stack.peek();
                if(ival[0] < top[1] && top[1] > ival[1]){
                        stack.pop();
                        stack.push(ival);
                }
                else if(ival[0] >= top[1]) stack.push(ival);
            }
        }
        return intervals.length - stack.size();
        
    }
}
