class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list) 
        for u,v, w in times:
            u -= 1 
            v -= 1
            graph[u].append((v, w)) 
        k -= 1 
        pq = [(0, k)]
        dist = [float('inf')] * n 
        dist[k] = 0 
        while pq:
            d, curr = heapq.heappop(pq) 
            for adj, w in graph[curr]:
                if dist[adj] > d + w:
                    heapq.heappush(pq, (d + w, adj)) 
                    dist[adj] = d + w 
        ans = max(dist) 
        if ans == float('inf'):
            return -1 
        return ans 