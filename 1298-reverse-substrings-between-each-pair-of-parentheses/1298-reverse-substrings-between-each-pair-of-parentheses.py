class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [] 
        curr = ''
        for c in s:
            print("stack: ", stack, " curr: ", curr)
            if c == '(':   
                stack.append(curr) 
                curr = ''
            elif c == ')':
                prev = '' 
                if stack:
                    prev = stack.pop() 
                curr = prev + curr[::-1]
            else:
                curr += c 
        return curr
