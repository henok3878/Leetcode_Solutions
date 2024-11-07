class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnts = [0] * 24
        for num in candidates:
            for i in range(24):
                if num & (1 << i):
                    cnts[i] += 1 
        return max(cnts)