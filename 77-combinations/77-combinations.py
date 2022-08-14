class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        ans = []
        def helper(i = 1,curr = []):
            if len(curr) == k:
                ans.append(curr[:]) 
                return 
            if i > n:
                return 
            #choose 
            curr.append(i) 
            helper(i + 1, curr)
            curr.pop() 
            #skip 
            helper(i + 1, curr)
        
        helper()
        return ans