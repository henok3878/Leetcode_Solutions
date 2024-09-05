class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        mappings = {')':'(', ']':'[','}':'{'}
        for c in s:
            if c in ["(", "[", '{']:
                stack.append(c) 
            else:
                curr = mappings[c]
                if len(stack) == 0 or stack[-1] != curr:
                    return False 
                stack.pop() 
        return len(stack) == 0