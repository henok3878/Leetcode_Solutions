# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        arr = [] 
        i = 0
        n = len(traversal)
        while i < n:
            j = i
            while j < n and traversal[j].isdigit():
                j += 1 
            
            if i != j:
                arr.append(int(traversal[i:j])) 
                i = j
            else:
                while j < n and traversal[j] == '-':
                    j += 1 
                if i != j:
                    arr.append(traversal[i:j])
                    i = j
                else:
                    i += 1                 
        def helper(st,end,d):
            if st > end:
                return None 
            elif st == end:
                return TreeNode(arr[st])
            target = '-'*(d + 1) 
            # print(arr[st:end + 1],target)
            if target in arr[st:end + 1]:
                t_st = arr.index(target,st, end + 1) 
                t_end  = end + 1
                if target in arr[t_st + 1:end + 1]:
                    t_end = arr.index(target,t_st + 1,end + 1)
                # print(t_st,t_end)
                return TreeNode(arr[st],helper(t_st + 1, t_end - 1,d + 1),helper(t_end + 1, end, d + 1))
            else:
                return None
            
        
        return helper(0,len(arr) - 1, 0)
            
            
    """
    "1-2--3---4-5--6---7"
     -
            1 
            
     2--3---4 , 5--6---7 
        2 
     3,None
    
    """