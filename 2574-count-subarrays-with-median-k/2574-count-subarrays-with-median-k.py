class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        new_nums = []
        k_idx = -1
        for i, num in enumerate(nums):
            if num == k:
                new_nums.append(0) 
                k_idx = i
            elif num > k:
                new_nums.append(1) 
            else:
                new_nums.append(-1)

        curr_sum = 0
        cnts = defaultdict(int)
        ans = 0
        for i in range(k_idx, -1,-1):
            curr_sum += new_nums[i] 
            if curr_sum == 1 or curr_sum == 0:
                ans += 1 
            cnts[curr_sum] += 1 
        curr_sum = 0
        for i in range(k_idx + 1, len(nums)):
            curr_sum += new_nums[i] 
            ans += cnts[-1 * curr_sum] + cnts[-1 * curr_sum + 1] 
        
        return ans 



        