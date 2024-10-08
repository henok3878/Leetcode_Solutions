class CustomInt:
    def __init__(self, num):
        self.num = num 
    def __lt__(self, other):
        return str(self.num) + str(other.num) < str(other.num) + str(self.num) 
    def __str__(self):
        return str(self.num)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [CustomInt(num) for num in nums] 
        nums.sort(reverse = True) 
        if str(nums[0]) == '0':
            return '0'
        return "".join([str(num) for num in nums])