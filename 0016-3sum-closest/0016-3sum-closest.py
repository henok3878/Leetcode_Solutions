from sortedcontainers import SortedList 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        best = float('inf')
        sl = SortedList() 
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                curr = nums[i] + nums[j] 
                best_comp = target - curr 
                k = bisect_left(sl, best_comp) 
                if(k < len(sl)):
                    op1 = curr + sl[k] 
                    if(abs(target - op1) < abs(target - best)):
                        best = op1
                if(k - 1 >= 0):
                    op2 = curr + sl[k - 1]
                    if(abs(target - op2) < abs(target - best)):
                        best = op2
                if (k + 1 < len(sl)): 
                    op3 = curr + sl[k + 1]
                    if(abs(target - op3) < abs(target - best)):
                        best = op3
                    
            sl.add(nums[i])
        return best 