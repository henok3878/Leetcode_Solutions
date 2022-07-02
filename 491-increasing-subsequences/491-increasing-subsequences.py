
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set() 
        
        def helper(idx, sofar):
            if idx == len(nums):
                if len(sofar) > 1:
                    res.add(tuple(sofar))
                return
            #skip 
            helper(idx + 1, sofar)
            #choose 
            if len(sofar) == 0 or sofar[-1] <= nums[idx]:
                sofar.append(nums[idx])
                helper(idx + 1, sofar)   
                sofar.pop()
        
        helper(0,[])
        
        ans = []
        for t in res:
            ans.append(list(t))
        
        return ans
        