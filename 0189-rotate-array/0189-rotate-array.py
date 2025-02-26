class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def reverse(arr, l, r):
            while l < r:
                nums[l],nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1 
        
        k = k % n 
        reverse(nums,0, n-k-1)
        reverse(nums,n-k,n-1)
        l = 0
        r = n - 1 
        while l < r: 
            nums[l], nums[r] = nums[r], nums[l] 
            l += 1 
            r -= 1 
    

        
        
        