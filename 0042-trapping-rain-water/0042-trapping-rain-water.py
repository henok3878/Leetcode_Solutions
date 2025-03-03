class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height) 
        stored = [0] * n  
        mx = height[0]
        for i in range(1, n):
            curr = height[i]
            if curr < mx:
                stored[i] = mx - curr 
            mx = max(curr, mx) 
        stored[-1] = 0
        mx = height[-1] 
        for i in range(n-2, -1,-1):
            curr = height[i] 
            if mx >= curr:
                stored[i] =min(stored[i], mx - curr) 
            else:
                stored[i] = 0 
            mx = max(curr, mx) 
        stored[0] = 0
        # print(stored)
        return sum(stored)