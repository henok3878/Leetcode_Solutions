class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort() 
        count = 1
        last = nums[0]
        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num - last > k:
                count += 1 
                last = curr_num 
        return count 