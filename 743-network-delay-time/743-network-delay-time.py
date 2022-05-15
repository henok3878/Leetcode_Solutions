class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for edge in times:
            graph[edge[0]].append((edge[1],edge[2]))
        queue = deque()
        queue.append((k,0))
        MAX = 10**20
        dist = [MAX] * (n + 1)
        dist[0] = -1
        dist[k] = 0
        while(len(queue) > 0):
            curr = queue.popleft()
            for adj in graph[curr[0]]:
                if(adj[1] + curr[1] < dist[adj[0]]):
                    queue.append((adj[0],adj[1] + curr[1]))
                    dist[adj[0]] = adj[1] + curr[1]        
        
        ans = max(dist)
        
        return -1 if ans == MAX else ans