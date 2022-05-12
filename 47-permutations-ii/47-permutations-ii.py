class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        
        ans = []
        seen = set()
        def permute(curr):
            if(len(curr) == n):
                ans.append(curr[:])
            prev = -100
            for nxt in range(n):
                if not nxt in seen and  prev != nums[nxt]:
                    curr.append(nums[nxt])
                    seen.add(nxt)
                    permute(curr)
                    prev = curr.pop()
                    seen.remove(nxt)
        permute([])
        return ans
                