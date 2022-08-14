class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        ans = []
        def helper(i = 1,curr = []):
            if len(curr) == k:
                ans.append(curr[:]) 
                return 
            for idx in range(i,n + 1):
                curr.append(idx)
                helper(idx + 1, curr)
                curr.pop()
        
        helper()
        return ans