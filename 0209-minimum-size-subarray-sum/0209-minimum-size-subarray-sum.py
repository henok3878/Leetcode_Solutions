class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        def is_pos(x):
            curr = 0
            for i in range(x):
                curr += nums[i] 
            mx = curr
            # print("x: ", x, "mx: ", mx)
            for i in range(1,len(nums)-x + 1):
                curr -= nums[i-1] 
                curr += nums[i + x - 1] 
                # print("curr: ", curr)
                mx = max(mx, curr) 
            return target <= mx 
        
        l = 1
        h = len(nums) 
        best = 0
        while l <= h:
            mid = (l + h) // 2 
            # print("mid: ", mid, "is_pos(mid): ", is_pos(mid))
            if is_pos(mid):
                h = mid - 1 
                best = mid 
            else:
                l = mid + 1 
        return best 
        



        