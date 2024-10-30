from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
      
        lis = [1] * n  # length up to index i
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        
        lds = [1] * n  # length starting at index i
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        #
        min_removals = float('inf')
        for i in range(1, n - 1):
            if lis[i] > 1 and lds[i] > 1:  # mountain peak
                min_removals = min(min_removals, n - (lis[i] + lds[i] - 1))

        return min_removals