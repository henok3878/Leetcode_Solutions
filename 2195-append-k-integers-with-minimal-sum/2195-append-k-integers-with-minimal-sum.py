class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        
        def get_sum(a):
            return a*(a + 1) // 2;  
        
        candidates = []
        prev = 0
        nums.sort() 
        for num in nums:
            if num - prev > 1:
                candidates.append((prev + 1, num - 1)) 
            prev = num 
        res = 0
        for c in candidates:
            if k == 0:
                return res 
            if c[1] - c[0] + 1 <= k:
                res += get_sum(c[1]) - get_sum(c[0]-1)
                k -= (c[1] - c[0] + 1) 
            else:
                res += get_sum(c[0] + (k - 1)) - get_sum(c[0] - 1) 
                k = 0 
        if k:
            res += get_sum(nums[-1] + k) - get_sum(nums[-1])
        return res 
        
