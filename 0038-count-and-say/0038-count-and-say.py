class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        for _ in range(1,n):
            say = ""
            prev = ""
            curr_cnt = 0
            for i in range(len(curr)):
                if curr[i] == prev:
                    curr_cnt += 1 
                else:
                    if curr_cnt > 0:
                        say += f"{curr_cnt}{prev}"
                    curr_cnt = 1
                    prev = curr[i]
            if curr_cnt > 0:
                say += f"{curr_cnt}{prev}"
            curr = say
        
        return curr

        