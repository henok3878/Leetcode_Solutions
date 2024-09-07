class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split('/') 
        stack = []
        for curr in files:
            if not curr or curr == '.':
                continue 
            elif curr == '..':
                if len(stack):
                    stack.pop() 
            else:
                stack.append(curr) 
        
        return "/" + "/".join(stack)
            