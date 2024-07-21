class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        N = len(nums)
        pos = [0] * N 
        neg = [0] * N 
        for i in range(N):
            diff = target[i] - nums[i] 
            if diff > 0:
                pos[i] = diff 
            elif diff < 0:
                neg[i] = abs(diff)
        # print(pos) 
        # print(neg)
        used = 0 
        prev = 0
        for i in range(N):
            curr = pos[i]
            if curr > prev:
                used += (curr - prev) 
            prev = curr
        prev = 0
        for i in range(N):
            curr = neg[i]
            if curr > prev:
                used += (curr - prev) 
            prev = curr
            
        return used
        
        
        