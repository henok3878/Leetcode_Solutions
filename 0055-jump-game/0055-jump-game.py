class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        closest_pos_idx = n - 1
        for i in range(n - 2,-1,-1):
            if(nums[i] + i >= closest_pos_idx):
                closest_pos_idx = i 
        return closest_pos_idx == 0