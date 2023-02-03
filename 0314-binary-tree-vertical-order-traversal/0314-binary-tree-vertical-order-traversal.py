# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_to_nodes = [[] for _ in range(2*100 + 2)]
        
        def dfs(node,col,row = 0):
            if not node:
                return 
            col_to_nodes[col+ 100].append((node.val,row))
            dfs(node.left, col - 1, row + 1) 
            dfs(node.right, col + 1, row + 1) 
        dfs(root, 0) 
        ans = []
        for i,nodes in enumerate(col_to_nodes):
            nodes.sort(key = lambda i : i[1])
            if nodes:
                ans.append([val for val,_ in nodes])
        return ans 