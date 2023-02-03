# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        col_to_nodes = [[] for _ in range(2*100 + 2)]
        
        q = deque([(root,0)]) 
        while q:
            node,col = q.popleft() 
            col_to_nodes[col + 100].append(node.val)
            if node.left:
                q.append((node.left,col - 1)) 
            if node.right:
                q.append((node.right, col + 1)) 
        ans = []
        for i,nodes in enumerate(col_to_nodes):
            if nodes:
                ans.append(nodes)
        return ans 
        