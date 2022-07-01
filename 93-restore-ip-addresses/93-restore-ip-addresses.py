class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(num):
            if len(num) > 1 and num[0] == '0':
                return False
            elif int(num) > 255:
                return False
            return True
        def restoreIpAddressesHelper(idx,dots,sofar):
            if idx >= len(s):
                return
            elif dots == 3:
                num4 = s[idx:]
                if is_valid(num4):
                    sofar.append(num4)
                    ans.append(".".join(sofar))
                    sofar.pop()
            for i in range(idx + 1, len(s)):
                num = s[idx:i]
                if not is_valid(num):
                    return 
                sofar.append(num)
                restoreIpAddressesHelper(i,dots + 1,sofar)
                sofar.pop()
            
        ans = []
        restoreIpAddressesHelper(0,0,[])            
        return ans
                        
        