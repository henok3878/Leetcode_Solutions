class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        res = k * (k + 1) // 2 
        nxt = k + 1
        for num in sorted(set(nums)):
            if num < nxt:
                res += (nxt - num)
                nxt += 1 
        return res 
        
