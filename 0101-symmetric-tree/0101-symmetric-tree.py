# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node1, node2):
            if node1 is None and node2 is None:
                return True 
            elif (node1 and node2 is None) or (node2 and node1 is None) or (node1.val != node2.val):
                return False
            return helper(node1.left, node2.right) and helper(node1.right, node2.left) 
        node1 = node2 = root 
        return helper(node1, node2)

