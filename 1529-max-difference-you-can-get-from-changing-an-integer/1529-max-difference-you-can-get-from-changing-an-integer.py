class Solution:
    def maxDiff(self, num: int) -> int:
        s_num = str(num)
        
        a = s_num
        for char_a in a:
            if char_a != "9":
                a = a.replace(char_a, "9")
                break
        
        b = s_num
        if b[0] != "1":
            b = b.replace(b[0], "1")
        else:
            for char_b in b[1:]:
                if char_b not in "01":
                    b = b.replace(char_b, "0")
                    break
        
        return int(a) - int(b)