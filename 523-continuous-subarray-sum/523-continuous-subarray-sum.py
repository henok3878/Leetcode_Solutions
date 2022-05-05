class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if(n < 2):
            return False
        
        p_sum = [0] * (n + 1)
        for i in range(n):
            p_sum[i + 1] = p_sum[i] + nums[i]
            
        mp = {}        
        for i in range(1,n+1):
            #print(i,p_sum,mp)
            if p_sum[i] % k == 0 and i > 1:
                return True
            
            elif p_sum[i] % k in mp:
                if (i - mp[p_sum[i] % k] > 1):
                    return True
            else: 
                mp[p_sum[i] % k] = i
        return False
        