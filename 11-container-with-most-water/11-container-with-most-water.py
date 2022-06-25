class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1 
        
        best = 0 
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            best = max(best, width * h)
            if height[left] >= height[right]:
                right -= 1 
            else:
                left += 1
        return best 