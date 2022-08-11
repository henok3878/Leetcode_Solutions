class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int) 
        
        for u,v in prerequisites: 
            graph[v].append(u) 
            indegree[u] += 1 
        q = deque() 
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i) 
        ans = [] 
        while q:
            curr = q.popleft() 
            ans.append(curr)
            for adj in graph[curr]:
                indegree[adj] -= 1 
                if indegree[adj] == 0:
                    q.append(adj)
        
        return ans if len(ans) == numCourses else []