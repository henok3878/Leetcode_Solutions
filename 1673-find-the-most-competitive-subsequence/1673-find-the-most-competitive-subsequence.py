class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = [] 
        n = len(nums)
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i] and ((n - i) + len(stack) - 1) >= k:
                stack.pop() 
            stack.append(i) 
        while len(stack) > k:
            stack.pop() 
        return [nums[i] for i in stack]