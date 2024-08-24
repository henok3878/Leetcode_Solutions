class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ["M", "D", "C", "L", "X", "V", "I"] 
        nums = [1000,500, 100, 50, 10, 5, 1] 
        specials = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'} 
        ans = ""
        for i,val in enumerate(nums):
            # print("num: ", num, end = " ")
            if num == 0:
                break
            elif(num in specials):
                ans += specials[num] 
                # print("curr: ", specials[num])
                break
            else:
                q = (num // val) 
                if(q > 0):
                    x = q * val 
                    if x in specials:
                        ans += specials[x] 
                        # print("curr: ", specials[x])
                    elif val in [50, 500]:
                        if val == 500:
                            qq = num // 100 
                            xx = qq * 100 
                            if xx in specials:
                                ans += specials[xx] 
                                x = xx
                            else:
                                ans += (q * symbols[i])
                        else:
                            qq = num // 10 
                            xx = qq * 10 
                            if xx in specials:
                                ans += specials[xx] 
                                x = xx
                            else:
                                ans += (q * symbols[i])
                    else:
                        ans += (q * symbols[i])
                        # print("curr: ", (q * symbols[i]))
                    num -= x
        return ans 
            
