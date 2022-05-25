class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        n = len(s)
        longest = 0
        stack.append(-1)
        
        for i,c in enumerate(s):
            
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        longest = max(longest, i - stack[-1])
                    else:
                        stack.append(i)
                        
        return longest
        
        """
        """