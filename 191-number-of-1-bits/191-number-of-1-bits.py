class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count  = 0
        while(n):
            n -= (n &-n)
            count += 1
        return count