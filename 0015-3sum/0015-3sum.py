class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        n = len(nums) 
        ans = [] 
        i = 0
        while i < n - 2:
            target = -(nums[i]) 
            j = i + 1
            k = n-1 
            while (j < k):
                val = (nums[j] + nums[k]) 
                if(val > target):
                    k -= 1 
                elif (val < target):
                    j += 1 
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while(j < k and nums[j] == nums[j + 1]): j+=1 
                    j += 1 
            while(i < n-1 and nums[i] == nums[i + 1]): i += 1 
            i += 1 
        return ans 