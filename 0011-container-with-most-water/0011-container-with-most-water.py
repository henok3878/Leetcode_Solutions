class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0 
        l = 0 
        r = len(height) - 1 
        while l < r:
            lheight = height[l] 
            rheight = height[r] 
            mx = max(mx, min(lheight, rheight) * (r - l)) 
            if (lheight <= rheight): l += 1 
            else: r -= 1
        return mx 