class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        offset = 10**5 
        mx = 0
        for i in range(len(nums)):
            nums[i] += offset 
            mx = max(nums[i], mx) 
        counter = [0] * (mx + 1) 
        for num in nums:
            counter[num] += 1 
        
        sorted_nums = []
        for i in range( mx + 1):
            freq = counter[i]
            sorted_nums += ([i - offset] * freq)
        
        return sorted_nums 
        
        