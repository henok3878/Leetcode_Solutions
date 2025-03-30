class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t) 
        count_t = Counter(t) 
        left = 0 
        l = float('inf')
        st = 0
        count_curr = Counter() 
        def check(counter1, counter2):
            for k, v  in counter2.items():
                if counter1[k] < v:
                    return False 
            return True 
            
        for right in range(m):
            ch = s[right] 
            count_curr[ch] += 1 
            if check(count_curr, count_t):
                curr_len = right - left + 1 
                if curr_len <= l:
                    st = left 
                    l = curr_len 
                # print(f"l: {left}, r: {right}, curr_cnt: {count_curr}")
                count_curr[s[left]] -= 1 
                left += 1 
                while(left <= right and check(count_curr, count_t)):
                    curr_len = right - left + 1 
                    if curr_len <= l:
                        st = left 
                        l = curr_len 
                    count_curr[s[left]] -= 1 
                    left += 1 
                
        if l == float('inf'):
            return ""
        return s[st: st + l] 
