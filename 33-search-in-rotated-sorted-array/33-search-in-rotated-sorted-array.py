class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find(target, st, end):
            idx = bisect_left(nums,target,st,end)
            if idx != end and target == nums[idx]:
                return idx 
            return -1 
        
            
        st, end = 0, len(nums) - 1 
        while st <= end:
            mid = (st + end ) // 2 
            if nums[mid] >= nums[0]: 
                st = mid + 1 
            else: 
                end = mid - 1 
        if st == len(nums):
            st -= 1 
        idx = find(target,st,len(nums))
        if idx != -1:
            return idx 
        return find(target,0, st)
