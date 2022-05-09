class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {'2':"abc", '3':"def",'4':"ghi",'5':"jkl",'6':"mno"
                   , '7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans = []
        def backtrack(i,digs,curr):
            
            if(i == len(digs)):
                nonlocal ans
                ans.append(''.join(curr))
                return
            for c in mappings[digs[i]]:
                #choose 
                curr.append(c)
                #explore 
                backtrack(i+1,digs,curr)
                #unchoose 
                curr.pop()
                
        backtrack(0,digits,[])
        
        return ans