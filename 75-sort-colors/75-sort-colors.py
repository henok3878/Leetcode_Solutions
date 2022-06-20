class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        red = 0
        white = 0
        blue = len(nums) - 1
        
        while white < len(nums):
            #print(nums,red,white,blue)
            if nums[white] == 2 and blue > white:
                nums[white],nums[blue] = nums[blue],nums[white]
                blue -= 1
            elif nums[white] == 0:
                nums[red],nums[white] = nums[white],nums[red]
                red += 1
                white += 1
            else:
                white += 1
        
                