class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ["M", "CM", "D", "CD", "C","XC" ,"L","XL" ,"X","IX", "V","IV", "I"] 
        nums = [1000,900,500,400, 100,90, 50, 40, 10, 9, 5,4, 1] 
        ans = ""
        for i,val in enumerate(nums):
            if num == 0:
                break
            else:
                q = (num // val) 
                if(q > 0):
                    x = q * val 
                    ans += (q * symbols[i])
                    num -= x
        return ans 
            
