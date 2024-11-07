class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnts = [0] * 24
        mx = 0
        for num in candidates:
            for i in range(24):
                cnts[i] += ((num >> i) & 1) 
                mx = max(cnts[i], mx)
        return mx