class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        visited = [False] * n 
        
        def permuteHelper(curr):
            if len(curr) == n:
                result.append(curr[:])
            
            for i in range(n):
                if(visited[i]):
                    continue
                
                curr.append(nums[i])
                visited[i] = True
                permuteHelper(curr)
                visited[i] = False
                curr.pop()
        
        permuteHelper([])
        
        return result
        
        