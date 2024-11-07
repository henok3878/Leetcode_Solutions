class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ''
        consec_cnt = 0
        for c in s:
            if ans and c == ans[-1]:
                if consec_cnt + 1 < 3:
                    consec_cnt += 1 
                    ans += c
            else:
                ans += c
                consec_cnt = 1
        return ans
            
            

            