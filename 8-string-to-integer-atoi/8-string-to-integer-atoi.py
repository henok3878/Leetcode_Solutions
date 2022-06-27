class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() 
        if not s:
            return 0
        sign,st = (1,0)
        if s[0] == '-':
            sign,st = -1,1
        elif s[0] == '+':
            st = 1 
        num = 0
        for i in range(st,len(s)):
            if not s[i].isdigit():
                break
            dig = ord(s[i]) - ord('0')
            num = num * 10 + dig 
        num *= sign 
        if num < -1*(2**31):
            return -1*(2**31)
        elif num > 2**31 -1:
            return 2**31 -1
        else:
            return num 