class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        def counter(s):
            n = len(s)
            zeros = 0
            ones = 0
            for i in range(n):
                if s[i] == "0":
                    zeros += 1
                else:
                    ones += 1
            return (zeros,ones)
        
        @cache 
        def dfs(i,curr):
            if i == len(strs):
                return 0
            select = MIN 
            if(curr[0] + count[i][0] <= m and curr[1] + count[i][1] <= n):
                select = 1 + dfs(i + 1, (curr[0] + count[i][0], curr[1] + count[i][1]))
            skip = dfs(i + 1, curr)
            
            return max(select,skip)
        
        count = []
        MIN = -1*(10 ** 20)
        for s in strs:
            count.append(counter(s))
            
        return dfs(0,(0,0))
        
        
    
            