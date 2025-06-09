class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count(prefix: int) -> int:
            total = 0
            low, high = prefix, prefix + 1
            while low <= n:
                total += min(n + 1, high) - low
                low *= 10
                high *= 10
            return total

        cur = 1
        k -= 1
        while k:
            nodes = count(cur)
            if nodes <= k:
                k -= nodes
                cur += 1
            else:
                k -= 1
                cur *= 10
        return cur
             
     