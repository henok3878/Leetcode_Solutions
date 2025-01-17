class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def helper(i, curr):
            if len(curr) == n:
                ans.append(curr[:]) 
                return 
            ith_num = nums[i]
            for j in range(i, n):
                jth_num = nums[j]
                curr.append(jth_num)
                nums[i], nums[j] = nums[j], nums[i]
                helper(i + 1, curr)
                nums[i], nums[j] = nums[j], nums[i]
                curr.pop() 
        helper(0, [])
        return ans 
                

