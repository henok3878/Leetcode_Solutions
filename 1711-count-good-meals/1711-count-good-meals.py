class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        """
        
        x + y = 2^i for i in range20 
        
        2^i - y = x 
        
        """
        MOD = 10**9 + 7 
        seen = defaultdict(int)
        count = 0
        for deli in deliciousness: 
            for i in range(22):
                num = 1 << i
                count += seen[num - deli] 
                count %= MOD 
            seen[deli] += 1 
        return count