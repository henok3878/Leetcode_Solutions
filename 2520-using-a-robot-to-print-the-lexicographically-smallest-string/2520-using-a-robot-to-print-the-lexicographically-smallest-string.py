class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        smallest_sofar  = chr(ord('z') + 1)
        suffix_smallest = [ s[i] for i in range(n)]

        for i in range(n-2, -1,-1):
            suffix_smallest[i] = min(s[i],suffix_smallest[i + 1]) 
        
        ans = []
        stack = []
        for i in range(n):
            curr_char = s[i] 
            curr_smallest = suffix_smallest[i]
            
            while stack and stack[-1] <= curr_smallest:
                ans.append(stack.pop())

            if curr_char == curr_smallest:
                ans.append(curr_char)
            else:
                stack.append(curr_char)
            
        stack.reverse() 
        return "".join(ans) + "".join(stack)