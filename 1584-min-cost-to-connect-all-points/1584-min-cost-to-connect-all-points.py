class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)
        visited = [False]*n

        min_heap = [(0,0)]
        heapify(min_heap)
        min_cost = 0
        
        used = 0
        while(used < n):
            cost,pt = heappop(min_heap)
            
            if(visited[pt]):
                continue;
            
            used += 1
            min_cost += cost
            visited[pt] = True
            
            for i in range(n):
                if(i != pt and not visited[i]):
                    dist = abs(points[pt][1] - points[i][1]) + abs(points[pt][0] - points[i][0])
                    heappush(min_heap,(dist,i))
        
        return min_cost