class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        redwhite = 0
        blue = len(nums) - 1
        while redwhite < blue:
            if nums[redwhite] == 2:
                nums[redwhite],nums[blue] = nums[blue],nums[redwhite]
                blue -= 1
            else:
                redwhite += 1
        if nums[blue] == 2:
            blue -= 1
        white = blue 
        red = 0
        while red < white:
            if nums[red] == 1:
                nums[red],nums[white] = nums[white],nums[red]
                white -= 1
            else:
                red += 1
        
                