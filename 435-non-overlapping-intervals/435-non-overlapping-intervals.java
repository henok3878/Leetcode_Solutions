class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->a[0] - b[0]);
        Stack<int[]> stack = new Stack<>();
        
        for(int[] ival : intervals){
            if(stack.isEmpty() || ival[0] >= stack.peek()[1]) stack.push(ival);
            else if(ival[0] < stack.peek()[1] && stack.peek()[1] > ival[1]){
                stack.pop();
                stack.push(ival);
            }
        }
        return intervals.length - stack.size();
        
    }
}

/*

*/