from sortedcontainers import SortedList 
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sl = SortedList() 
        for i,num in enumerate(nums):
            if len(sl) > k:
                sl.remove(nums[i - k - 1])
            l = sl.bisect_left(nums[i] - t)
            r = sl.bisect_left(nums[i] + t) 
            
            if l < len(sl) and nums[i] - t <= sl[l] <= nums[i] + t:
                return True 
            if r < len(sl) and nums[i] - t <= sl[r] <= nums[i] + t:
                return True 
            sl.add(nums[i])
        return False
                