class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort() 
        i = 0 
        def nxt(nums, i, dir = 1):
            n = len(nums) 
            while i + dir >= 0 and i + dir < n and nums[i + dir] == nums[i]:
                i += dir 
            return i + dir 

        while(i < n):
            num1 = nums[i] 
            j = i + 1 
            k = n - 1 
            # num1 + num2 + num3 = 0 
            # num2 + num3 = -num1 
            target = -1 * num1 
            while (j < k):
                num2 = nums[j] 
                num3 = nums[k] 
                if(num2 + num3 > target):
                    k = nxt(nums, k, dir = -1)
                else:
                    if (num2 + num3 == target):
                        ans.append((num1, num2, num3)) 
                    j = nxt(nums, j)
            i = nxt(nums, i) 
        return ans 

# -4, -1, -1, 0, 1, 2, 