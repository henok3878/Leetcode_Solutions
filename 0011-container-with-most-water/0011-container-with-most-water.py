class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1 

        ans = 0 
        while(l < r):
            left = height[l] 
            right = height[r]
            ans = max(ans, min(left, right) * (r - l))
            if(left > right):
                r -= 1
            else:
                l += 1 
        return ans 