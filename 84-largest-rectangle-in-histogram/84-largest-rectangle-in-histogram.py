class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prev_smaller = [-1] * n  
        nxt_smaller = [n] * n 
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                nxt_smaller[stack.pop()] = i 
            stack.append(i) 
        stack.clear() 
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] > heights[i]:
                prev_smaller[stack.pop()] = i 
            stack.append(i)     
        
        ans = 0 
        for i in range(n):
            ans = max(ans,heights[i]*(nxt_smaller[i] - prev_smaller[i] - 1)) 
        return ans 