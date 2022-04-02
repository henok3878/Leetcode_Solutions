class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] nextGreater = new int[n];
        
        int right = height[n-1], left = height[0];
        for(int i = n-1; i >= 0; i--){
            if(height[i] > right) right = height[i];
            nextGreater[i] = right;
        }
        int ans = 0;
        
        for(int i = 0; i < n; i++){
            if(height[i] > left) left = height[i];
            ans += Math.min(left,nextGreater[i]) - height[i];
            
        }
        
        return ans;
    }
}
