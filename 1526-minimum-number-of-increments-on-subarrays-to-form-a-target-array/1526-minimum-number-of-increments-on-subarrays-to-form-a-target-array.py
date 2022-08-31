class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0 
        for i,num in enumerate(target):
            if i == 0:
                ans += target[0] 
            else: 
                if target[i - 1] <= num:
                    ans += num - target[i-1]
        
        return ans 
                    
                    