# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        leaves = []
        def is_leaf(node):
            return node and node.left is None and node.right is None 

        def connect_parent(node, parent):
            if not node:
                return 
            elif node.left is None and node.right is None:
                leaves.append(node) 
            node.parent = parent 
            connect_parent(node.left, node) 
            connect_parent(node.right, node) 
        
        connect_parent(root, None) 
        ans = 0 
        for leave in leaves:
            q = deque() 
            q.append((leave, 0, None)) 
            while q:
                curr, d, p = q.popleft() 
                if is_leaf(curr) and (0 < d <= distance):
                    ans += 1 
                if curr.left and curr.left != p:
                    q.append((curr.left, d + 1, curr)) 
                if curr.right and curr.right != p:
                    q.append((curr.right, d + 1, curr))
                if curr.parent and curr.parent != p:
                    q.append((curr.parent, d + 1, curr)) 

        return ans // 2