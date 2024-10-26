class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0 
        right = 0
        n = len(nums) 
        ans = 0
        curr_sum = 0
      
        for right in range(n):
            curr_sum += nums[right] 
            size = right - left + 1 
            while size * curr_sum >= k:
                curr_sum -= nums[left]
                size -= 1 
                left += 1 
            ans += size

        return ans
            







"""
nums = [2,1,4,3,5], k = 10

subarrays: 

"""