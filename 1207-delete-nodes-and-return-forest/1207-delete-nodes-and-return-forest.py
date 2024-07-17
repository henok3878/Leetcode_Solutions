# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete) # O(n) 
        ans = []

        def dfs(node, parent, isL):
            if node is None:
                return 
            l = node.left 
            r = node.right 
            if node.val in to_delete:
                if parent:
                    if(isL):
                        parent.left = None 
                    else:
                        parent.right = None 
                dfs(l, None,True)
                dfs(r, None, False)
            else:
                if parent is None:
                    ans.append(node) 
                dfs(l, node, True)
                dfs(r, node, False) 
            

        dfs(root, None, False) 

        return ans 

                

