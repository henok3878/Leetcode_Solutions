class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1" 
        cnt = self.countAndSay(n - 1) 
        say = ""
        prev = ""
        curr_cnt = 0
        for i in range(len(cnt)):
            if cnt[i] == prev:
                curr_cnt += 1 
            else:
                if curr_cnt > 0:
                    say += f"{curr_cnt}{prev}"
                curr_cnt = 1
                prev = cnt[i]
        if curr_cnt > 0:
            say += f"{curr_cnt}{prev}"
        return say 

        