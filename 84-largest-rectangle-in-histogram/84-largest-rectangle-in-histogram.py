class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] 
        heights.append(0)
        n = len(heights)
        ans = 0
        for i in range(n):
            while len(stack) > 1 and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()] 
                ans = max(ans,h * (i - stack[-1] - 1))
            stack.append(i)
        return ans 