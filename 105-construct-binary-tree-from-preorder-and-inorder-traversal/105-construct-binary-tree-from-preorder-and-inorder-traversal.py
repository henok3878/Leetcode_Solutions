# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {}
        for i,node in enumerate(inorder):
            inorder_idx[node] = i 
            
        def helper(in_st,in_end,pr_st,pr_end):
            # print(in_st,in_end,pr_st,pr_end)
            if in_end <= in_st and pr_st >= pr_end: 
                return TreeNode(inorder[in_st]) if in_st <= in_end else None 
            root = preorder[pr_st] 
            root_idx = inorder_idx[root] 
            left_size = root_idx - in_st 
            return TreeNode(preorder[pr_st], helper(in_st,root_idx - 1,pr_st + 1, pr_st + left_size), helper(root_idx + 1,in_end,pr_st + 1 + left_size, pr_end))
        
        n = len(inorder) 
        return helper(0,n-1,0,n-1) 