class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return 
        mapping = {"2":"abc","3":"def", "4": "ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        ans = []
        def back_track(i,curr):
            if i == len(digits):
                ans.append("".join(curr))
                return
            for key in mapping[digits[i]]:
                curr.append(key)
                back_track(i + 1, curr)
                curr.pop() 
        
        back_track(0,[])
        return ans