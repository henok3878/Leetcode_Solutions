class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list) 
        for i in range(n):
            x,y, r = bombs[i]
            for j in range(n):
                if i == j: continue 
                xx, yy, _ = bombs[j]
                dist = ((xx - x) ** 2 ) + ((yy - y) ** 2) 
                if dist <= r ** 2:
                    graph[i].append(j) 


        visited = set()
        
        def helper(i):
            if i >= n or i in visited:
                return 0
            visited.add(i)
            total = 1
            for j in graph[i]:
                total += helper(j) 
            return total 
        
        ans = 0 
        for i in range(n):
            ans = max(ans, helper(i)) 
            visited.clear()
        
        return ans
            