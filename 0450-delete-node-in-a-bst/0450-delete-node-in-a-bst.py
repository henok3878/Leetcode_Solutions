# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return

        def is_leaf(node):
            return node.left is None and node.right is None 

        def get_min(node):
            if node.left:
                return get_min(node.left)
            return node.val

        if root.val == key:
            if is_leaf(root):
                return None 
            elif root.right:
                root.val = get_min(root.right)
                root.right = self.deleteNode(root.right,root.val)
            else:
                root = root.left

        elif key < root.val:
            root.left = self.deleteNode(root.left, key) 
        else:
            root.right = self.deleteNode(root.right, key) 

        return root 

        
