class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for i in range(1,len(target)):
            num = target[i]
            if target[i - 1] <= num:
                ans += num - target[i-1]
        
        return ans 
                    
                    