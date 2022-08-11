class Solution:
    
    def sumSubarrayMins(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        min_stack = [] 
        n = len(nums) 
        total_sum = 0 
        for i in range(n): 
            while min_stack and nums[i] < nums[min_stack[-1]]:
                prev_idx = min_stack.pop() 
                prev_prev = -1 if not min_stack else min_stack[-1]
                total_sum += ((i - prev_idx)* (prev_idx - 1 - prev_prev)) * nums[prev_idx]  + ((i - prev_idx) * nums[prev_idx])  
                total_sum %= MOD 
                
            min_stack.append(i)
            
        
        while min_stack:
            prev_idx = min_stack.pop() 
            prev_prev = -1 if not min_stack else min_stack[-1]
            total_sum += ((n - prev_idx)* (prev_idx - 1 - prev_prev)) * nums[prev_idx] + ((n - prev_idx) * nums[prev_idx])
            total_sum %= MOD 

            
        return total_sum 