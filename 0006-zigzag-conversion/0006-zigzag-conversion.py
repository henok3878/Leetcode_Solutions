class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)] 
        dig_mode = False 
        level = 0
        n = len(s)
        for i in range(n):
            ans[level].append(s[i]) 
            if dig_mode:
                level -= 1 
            else:
                level += 1 
            if(level >= numRows - 1):
                dig_mode = True  
                level = numRows - 1 
            if level <= 0:
                dig_mode = False 
                level = 0 
            
        return "".join(["".join(level) for level in ans])  