class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points,(a,b)-> Integer.compare(a[0],b[0]));
        Stack<int[]> stack = new Stack();
        for(int[] interval : points){
            if(stack.isEmpty()) stack.push(interval);
            else{
                int[] top = stack.peek();
                if(interval[0] <= top[1]){
                    int end = Math.min(top[1],interval[1]);
                    stack.pop();
                    stack.push(new int[]{interval[0],end});
                }else if(interval[0] > top[1]) stack.push(interval);
            }
        }
        return stack.size();
    }
}

/*
st: 9:00
sub: 9:20 
    

[[10,16],[2,8],[1,6],[7,12]]

1  -  6 
   2  - 8 
      7  -  12
        10  -   16



*/