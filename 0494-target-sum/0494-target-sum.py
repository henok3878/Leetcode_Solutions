class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache 
        def findWays(i,amt):
            if i >= len(nums):
                if amt == target:
                    return 1
                return 0
            # choose +
            op1 = findWays(i + 1, amt + nums[i])
            # choose - 
            op2 = findWays(i + 1, amt - nums[i]) 

            return op1 + op2 
        
        return findWays(0, 0)


"""
Exploring every possilbe ways of building expression and evaluating the result. 

To do this, we can use recurssion:
    - For each number we can explore two paths:
        1) with + 
        2) with - 
    - The recurssion state is gonna be (idx,curr_val):
        - path1 = (idx + 1, curr_val + nums[idx]) 
        - path2 = (idx + 1, curr_val -  nums[idx])
        - res = path1 + path2 
    - base case: 
        - if (idx >= n):
            if target == curr_val): return 1
            return 0

    - The time complexity: 2**n 
    - eventhough the total function call is exponential (2**n), the actual unique states (unique combinations of function params) are only n * (max_sum) so we can avoid repetitive calls by storing intermidate results. 

"""