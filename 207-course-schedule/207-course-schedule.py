class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses_taken = 0 
        graph = defaultdict(list) 
        indegree = defaultdict(int) 
        
        for a,b in prerequisites: 
            graph[b].append(a) 
            indegree[a] += 1 
        
        q = deque()
        
        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node) 
        #print(q)
        while q:
            curr = q.popleft() 
            courses_taken += 1 
            
            for adj in graph[curr]:
                indegree[adj] -= 1 
                if indegree[adj] == 0:
                    q.append(adj) 
        
        if courses_taken == numCourses: 
            return True 
        else:
            return False 