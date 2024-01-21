class Solution:
    def rob(self, nums: List[int]) -> int:
        dont_rob = 0 
        do_rob = nums[0]
        for i in range(1,len(nums)):
            temp = do_rob 
            do_rob = dont_rob + nums[i] 
            dont_rob = max(temp,dont_rob) 
        return max(do_rob, dont_rob)
            