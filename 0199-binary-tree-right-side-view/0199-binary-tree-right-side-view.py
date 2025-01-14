# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root: 
            return []
        q = deque([root]) 
        while q:
            s = len(q)
            curr = None 
            for _ in range(s):
                curr = q.popleft() 
                if curr.left:
                    q.append(curr.left) 
                if curr.right:
                    q.append(curr.right)
            if curr:
                ans.append(curr.val)
        return ans 


            