class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        prev_cnt = 0
        n = len(nums)
        ans = []
        for i in range(n):
            cnt = 0
            if i > 0 and ((nums[i]-nums[i - 1]) == 1):
                cnt += prev_cnt 
            cnt += 1

            if cnt >= k:
                ans.append(nums[i]) 
            elif i >= (k - 1):
                ans.append(-1)  
            prev_cnt = cnt 
        
        return ans 