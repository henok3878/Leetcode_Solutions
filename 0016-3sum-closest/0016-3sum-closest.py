from sortedcontainers import SortedList 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        n = len(nums)
        best = float('inf')
        for i in range(n-2):
            j = i + 1
            k = n - 1 
            while(j < k):
                curr = nums[i] + nums[j] + nums[k] 
                if(abs(curr - target) < abs(best - target)):
                    best = curr 
                if curr > target:
                    k -= 1 
                else:
                    j += 1 
        return best 
