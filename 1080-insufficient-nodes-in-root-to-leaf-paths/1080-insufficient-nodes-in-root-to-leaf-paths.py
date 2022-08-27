# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        
        def dfs(node,path_sum):
            if node.left is None and node.right is None:
                return path_sum + node.val 
            
            left = dfs(node.left, path_sum + node.val) if node.left else float('-inf')
            right = dfs(node.right, path_sum + node.val)  if node.right else float('-inf')
            if left < limit:
                node.left = None 
            if right < limit: 
                node.right = None 
            return max(left, right)
        
        dummy = TreeNode(val = 0,left = None, right = root)
        res = dfs(dummy,0)
        return dummy.right