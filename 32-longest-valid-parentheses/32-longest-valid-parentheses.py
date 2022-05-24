class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [] 
        max_len = 0
        last_unmatched_end = -1


        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            else:
                if stack:
                    # remove the matched parenthesis
                    stack.pop()
                    if stack:
                        last_unmatched_open = stack[-1]
                        max_len = max(max_len, i - last_unmatched_open)
                    else:
                        max_len = max(max_len, i - last_unmatched_end)
                else:
                    last_unmatched_end = i
        return max_len