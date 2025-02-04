class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list) 
        for u,v, w in times:
            u -= 1 
            v -= 1
            graph[u].append((v, w)) 
        k -= 1 
        q = deque([(k, 0)])
        dist = [float('inf')] * n 
        dist[k] = 0 
        while q:
            curr, d = q.popleft() 
            for adj, w in graph[curr]:
                if dist[adj] > d + w:
                    q.append((adj, d + w)) 
                    dist[adj] = d + w 
        ans = max(dist) 
        if ans == float('inf'):
            return -1 
        return ans 