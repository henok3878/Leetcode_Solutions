# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list) 
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft() 
            if curr.left:
                graph[curr.val].append(curr.left.val) 
                graph[curr.left.val].append(curr.val)
                q.append(curr.left)
            if curr.right:
                graph[curr.val].append(curr.right.val)
                graph[curr.right.val].append(curr.val)
                q.append(curr.right)
        
        q = deque() 
        q.append((start,-1, 0))
        # print(graph)
        ans = 0
        while q:
            curr, p, lvl = q.popleft() 
            ans = max(lvl, ans)
            for adj in graph[curr]:
                if adj == p:
                    continue 
                q.append((adj, curr, lvl + 1)) 
        return ans 
                

            
            
            
            