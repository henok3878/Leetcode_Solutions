class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = collections.deque()
        n = len(s)
        
        for i in range(n):

            if stack and stack[-1][0] == s[i]:
                c,cnt = stack.pop()
                stack.append((c,cnt + 1))
            else:
                stack.append((s[i],1))
                
            if stack and stack[-1][1] == k:
                stack.pop()
        ans = []
        for c,cnt in stack:
            ans.append(c*cnt)
        return ''.join(ans)
                