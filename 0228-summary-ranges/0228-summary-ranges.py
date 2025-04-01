class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums.append(float('inf'))
        n = len(nums)  
        ans = []
        left = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i - 1] + 1:
                if (nums[i-1] == left):
                    ans.append(f"{left}")
                else:
                    ans.append(f"{left}->{nums[i-1]}")
                left = nums[i] 
        return ans 

