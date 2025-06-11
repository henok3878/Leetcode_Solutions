class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        
        prefix = [[0]*(n + 1) for _ in range(5)]
        for i, ch in enumerate(s):
            d = ord(ch) - ord('0')
            for c in range(5):
                prefix[c][i + 1] = prefix[c][i] + (c == d)

        ans     = -10**9

        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                # state = (parity_a << 1) | parity_b   (00, 01, 10, 11)
                # min_at_cnt[state][cnt_b] = smallest diff (cnt_a - cnt_b)
                min_at_cnt = [[10**9]*(n + 1) for _ in range(4)]
                best_min   = [10**9]*4      
                ptr        = [st & 1 for st in range(4)]   

                for r in range(1, n + 1):
                    ca_r = prefix[a][r]
                    cb_r = prefix[b][r]

                    if r >= k:
                        l      = r - k
                        ca_l   = prefix[a][l]
                        cb_l   = prefix[b][l]
                        state  = (ca_l & 1) << 1 | (cb_l & 1)
                        diff_l = ca_l - cb_l

                        if diff_l < min_at_cnt[state][cb_l]:
                            min_at_cnt[state][cb_l] = diff_l

                        if cb_l <= cb_r - 2 and diff_l < best_min[state]:
                            best_min[state] = diff_l

                    thresh = cb_r - 2   
                    for state in range(4):
                        while ptr[state] <= thresh:
                            if min_at_cnt[state][ptr[state]] < best_min[state]:
                                best_min[state] = min_at_cnt[state][ptr[state]]
                            ptr[state] += 2  

                    if r >= k and cb_r >= 2:
                        need = ((ca_r & 1) ^ 1) << 1 | (cb_r & 1)
                        if best_min[need] != 10**9:
                            diff_r = ca_r - cb_r
                            ans = max(ans, diff_r - best_min[need])

        return -1 if ans == -10**9 else ans
 