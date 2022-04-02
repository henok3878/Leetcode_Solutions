class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] nextGreater = new int[n];
        int[] prevGreater = new int[n];
        
        int right = height[n-1], left = height[0];
        for(int i = n-1; i >= 0; i--){
            if(height[i] > right) right = height[i];
            nextGreater[i] = right;
        }
        
        for(int i = 0; i < n; i++){
            if(height[i] > left) left = height[i];
            prevGreater[i] = left;
        }
        
        int ans = 0;
        for(int i = 0;i < n;i++){
          ans += Math.min(prevGreater[i],nextGreater[i]) - height[i];
        }
        
        return ans;
    }
}

/*
- When does a water is trapped?

        if I have elem with greater elev, water gets trapped between us.
        
        // find the greatest to right of me 
        // find the greatest to left of me  
        
        
        trapped water at ith index = min(leftGreatest,rightGreatest) - currHeight;

*/