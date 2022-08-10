class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [[0,0] for  _ in range(n)] 
        for curr_idx in range(n):
            curr_num = nums[curr_idx]
            for prev_idx in range(curr_idx):
                if nums[prev_idx] < curr_num: 
                    dp[curr_idx][0] = max(dp[prev_idx][1] + 1, dp[curr_idx][0])
                elif nums[prev_idx] > curr_num: 
                    dp[curr_idx][1] = max(dp[prev_idx][0] + 1, dp[curr_idx][1]) 
        
        return max(dp[n-1][0], dp[n-1][1]) + 1