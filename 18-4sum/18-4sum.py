class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a + 1,n):
                if b > a + 1 and nums[b] == nums[b-1]:
                    continue 
                c = b + 1 
                d = n - 1 
                while c < d:
                    four_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    if four_sum == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1  
                        d -= 1 
                        while c < n and nums[c] == nums[c - 1]:
                            c += 1 
                        while d > c and nums[d] == nums[d + 1]:
                            d -= 1 
                    elif four_sum > target:
                        d -= 1 
                    else:
                        c += 1 
        return ans 