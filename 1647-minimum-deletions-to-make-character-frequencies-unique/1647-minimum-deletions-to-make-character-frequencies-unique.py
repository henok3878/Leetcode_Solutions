class Solution:
    def minDeletions(self, s: str) -> int:
        """
        
        3,3,2
        3,3,2 = 8
        3 + 2 + 1 = 6 
        
        8 - 6 
        
        """
        counter = Counter(s) 
        max_c = max(counter.values()) 

        visited = set() 
        counts = []
        for k,v in counter.items():
            counts.append(v)
        counts.sort(key = lambda i: -i) 
        ans = 0 
        for v in counts:
            while v != 0 and v in visited:
                v -= 1 
                ans += 1 
            visited.add(v)
        return ans 
        