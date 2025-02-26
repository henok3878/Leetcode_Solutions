class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0 
        major = None 
        for num in nums:
            if cnt == 0:
                major = num 

            if major == num:
                cnt += 1 
            else:
                cnt -= 1
        return major 