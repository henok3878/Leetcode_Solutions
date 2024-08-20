class Solution:
    def minMaxDifference(self, num: int) -> int:
        first_idx = 0 
        str_num = str(num)
        while(first_idx < len(str_num) and str_num[first_idx] == '9'):
            first_idx += 1 
        if(first_idx == len(str_num)):
            return num 
        else:
            first_idx_el = str_num[first_idx] 
            mx_str = ''
            for c in str_num:
                if c == first_idx_el:
                    mx_str += '9'
                else:
                    mx_str += c 
            mn_str = ''
            first_el = str_num[0] 
            mn_str = ''
            for c in str_num:
                if c == first_el:
                    if(len(mn_str) > 0):
                        mn_str += '0'
                else:
                    mn_str += c 
            mn = 0 
            if(mn_str):
                mn = int(mn_str)
            # print("mx,mn: " , mx_str, mn_str)
            return int(mx_str) - mn
            