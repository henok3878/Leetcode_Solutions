class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2  # mid never equals high
            if nums[mid] == target:
                return mid 
            elif nums[mid] > target:
                high = mid 
            else:
                low = mid + 1
        return -1
