class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [0] * n 
        stack = [0]
        for i in range(1,n):
            t = 0 
            while stack and nums[stack[-1]] <= nums[i]:
                t = max(t, steps[stack[-1]])
                stack.pop()
            if stack:
                steps[i] = t + 1
            stack.append(i)
        # print(steps)
        return max(steps)
                
                
                
                
        """
        i -> i + 1 
           > 
        
        i -> i + 2 
        
        i -> n - 1 
        
        [10,1,2,3,4,5,6,1,2,3]
        
        
        cases: 
            -> Remove every element that has a greater element to the left 
            -> Decreasing: 
                 steps: 1 
                 output: []
            -> [1,3,4,8,6,6,5,7,2,1]
                0 1 2 3 4 5 6 7 8 9 
                
            -> steps = [0,0,0,0,1,1,2,1,1]
                                  
                
            
        """