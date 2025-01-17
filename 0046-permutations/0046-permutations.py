class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def helper( curr):
            if(len(curr) == n):
                ans.append(curr[:]) 
            for i in range(n):
                if nums[i] in curr:
                    continue 
                curr.append(nums[i])
                helper(curr) 
                curr.pop()
        
        helper([]) 
        return ans 
                

