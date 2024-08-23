class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_mx = [0] * n
        mx = height[0]
        for i in range(1,n):
            left_mx[i] = mx 
            mx = max(mx, height[i]) 
        ans = 0 
        mx = 0
        for i in range(n - 1, -1,-1):
            min_mx = min(left_mx[i], mx) 
            ans += max(0, min_mx - height[i]) 
            mx = max(height[i], mx)
        
        return ans 

        