class Solution:
    def jump(self, nums: List[int]) -> int:
        best = 0 
        curr = 0
        cnt = 0 
        for i, num in enumerate(nums):
            # print(i,curr, best, cnt)
            if i > curr: 
                cnt += 1 
                curr = best 
            if(nums[i] + i > best):
                best = nums[i] + i 

        return cnt 