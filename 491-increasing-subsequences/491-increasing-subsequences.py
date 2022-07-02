
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def helper(idx, sofar):
            
            if len(sofar) > 1:
                res.append(sofar[:])

            visited = set()
            for i in range(idx,len(nums)):
                if nums[i] in visited:
                    continue 
                if len(sofar) == 0 or sofar[-1] <= nums[i]:
                    visited.add(nums[i])
                    sofar.append(nums[i])
                    helper(i + 1,sofar)
                    sofar.pop()
        
        helper(0,[])   
        return res
        