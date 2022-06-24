class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = -1
        idx = -1 
        for i in reversed(range(n)):
            if nums[i] < p:
                idx = i 
                break
            p = nums[i]
        if idx == -1:
            return nums.reverse()

        nxt_greater,nxt_greater_idx = 101 ,-1 
        for i in range(idx, n):
            if nums[idx] < nums[i] and nums[i] <= nxt_greater:
                nxt_greater = nums[i]
                nxt_greater_idx = i 
        # swap 
        nums[idx], nums[nxt_greater_idx] = nums[nxt_greater_idx] , nums[idx]
        # reverse after idx + 1 
        nums[idx + 1 : ] = reversed(nums[idx+1:])