class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr + [0]
        n = len(arr)
        stack = [0]
        ans = 0
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop() 
                ends = (i - idx) 
                sts = (idx - stack[-1]) 
                ans += (arr[idx]) * (ends * sts)
            stack.append(i) 
        return ans % (10**9 + 7)
    
        
        