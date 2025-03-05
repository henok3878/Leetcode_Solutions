class Solution:
    def intToRoman(self, num: int) -> str:
        mappings = {1:"I",4:"IV", 5:"V", 9:"IX", 10:"X",40:"XL", 50:"L",90:"XC",100:"C",
        400:"CD", 500:"D", 900: "CM",1000:"M"}
        ans = ''
        for k in reversed(mappings.keys()):
            while num >= k:
                num -= k 
                ans += mappings[k]
        return ans 
