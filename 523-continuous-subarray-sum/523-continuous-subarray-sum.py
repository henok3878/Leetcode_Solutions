class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if(n < 2):
            return False
        p_sum = 0       
        mp = {}        
        for i in range(0,n):
            p_sum += nums[i]
            #print(i,p_sum,mp)
            if p_sum % k == 0 and i >= 1:
                return True
            
            elif p_sum % k in mp:
                if (i - mp[p_sum % k] > 1):
                    return True
            else: 
                mp[p_sum % k] = i
        return False
        