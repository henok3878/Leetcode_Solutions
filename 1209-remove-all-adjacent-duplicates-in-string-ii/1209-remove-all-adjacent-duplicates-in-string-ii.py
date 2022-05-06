class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = collections.deque()
        n = len(s)
        
        for i in range(n):

            if len(stack) != 0 and stack[-1][0] == s[i]:
                c,cnt = stack.pop()
                stack.append((c,cnt + 1))
            else:
                stack.append((s[i],1))
                
            if len(stack) > 0 and stack[-1][1] == k:
                stack.pop()
        ans = []
        while(len(stack) > 0):
            ans.insert(0,stack[-1][0]*stack.pop()[1])
        
        return ''.join(ans)
                