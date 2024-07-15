# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = {}
        not_root = set() 
        for p,c,isL in descriptions:
            if p not in tree: 
                tree[p] = TreeNode(p) 
            curr = tree[p] 

            if(c not in tree):
                tree[c] = TreeNode(c)
                
            if(isL == 1):
                curr.left = tree[c]
            else:
                curr.right = tree[c] 
            not_root.add(c) 
        for p,_,_ in descriptions:
            if p not in not_root:
                return tree[p]
        return None

        
        