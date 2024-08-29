class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board) 
        board.reverse()
        l = [-1] * (n ** 2)
        for i in range(n):
            for j in range(n):
                idx = (i * n) + (j if i % 2 == 0 else (n - 1 - j))
                l[idx] = board[i][j]
        visited = [False] * (n ** 2 + 1)
        dist = [-1] * ( n ** 2) 
        q = deque() 
        q.append(0)
        visited[0] = True 
        dist[0] = 0 

        while q:
            curr = q.popleft() 
            for nxt in range(curr + 1, min(n**2,curr + 7)):
                if l[nxt] != -1:
                    nxt = l[nxt] - 1
                if not visited[nxt]:
                    q.append(nxt) 
                    visited[nxt] = True 
                    dist[nxt] = dist[curr] + 1
        return dist[n**2 - 1]

