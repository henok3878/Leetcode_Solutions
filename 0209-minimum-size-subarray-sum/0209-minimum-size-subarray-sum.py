class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = r = curr = 0
        ans = float('inf')

        while l < n or r < n:

            if curr < target:
                if r < n:
                    curr += nums[r]
                    r += 1
                else:
                    break
            else:
                ans = min(ans, r - l)
                # print("curr:", curr, "l:", l,"r:",r)
                curr -= nums[l]
                l += 1
        return ans if ans != float('inf') else 0
