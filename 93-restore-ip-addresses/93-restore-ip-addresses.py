class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(num):
            if len(num) > 1 and num[0] == '0':
                return False
            elif int(num) > 255:
                return False
            return True
        ans = []
        n = len(s)
        for fst in range(1,n):
            num1 = s[:fst]
            if not is_valid(num1):
                continue
            for snd in range(fst + 1, n):
                num2 = s[fst:snd]
                if not is_valid(num2):
                    continue
                for thrd in range(snd + 1, n):
                    num3 = s[snd:thrd]
                    if not is_valid(num3):
                        continue
                    num4 = s[thrd:]
                    if not is_valid(num4):
                        continue
                    ans.append(num1 + "." + num2 + "." + num3 + "." + num4)
                    
        return ans
                        
        