class Solution:
    def largestPalindromic(self, num: str) -> str:
        counts = [0] * 10 
        for c in num:
            counts[int(c)] += 1 
        
        evens = [0] * 10 
        for k,v in enumerate(counts):
            evens[k] = v // 2 
            counts[k] = v % 2
        ans = []
        zero = False
        for i in range(9,-1,-1):
            if evens[i] > 0:
                if not ans and i == 0:
                    zero = True
                    break
                ans.append(str(i) * evens[i]) 
        rev = ans[::-1]
        for i in range(9,-1,-1):
            if counts[i] > 0:
                ans += str(i)
                break 
        ans += rev 
        if not ans and zero:
            return '0'
        
        return "".join(ans)