class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        last_val_idx = n - 1
        i = 0
        while (i <= last_val_idx):
            if(nums[i] == val):
                nums[i], nums[last_val_idx] = nums[last_val_idx], nums[i] 
                last_val_idx -= 1 
            else:
                i += 1
        return (n - (n - 1 - last_val_idx))