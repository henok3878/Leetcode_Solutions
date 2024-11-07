class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        mx = 0
        for i in range(24):
            curr_cnt = 0
            for num in candidates:
                curr_cnt += ((num >> i) & 1) 
                mx = max(mx, curr_cnt)
        return mx