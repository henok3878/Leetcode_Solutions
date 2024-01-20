class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        right = [n] * n 
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                right[stack[-1]] = i 
                stack.pop() 
            stack.append(i) 
        stack2 = []
        for i in range(n-1,-1,-1):
            while stack2 and arr[stack2[-1]] >= arr[i]:
                left[stack2[-1]] = i 
                stack2.pop() 
            stack2.append(i) 
        # print(stack)
        # print(stack2)
        ans = 0 
        for i in range(n):
            sts = i - left[i]
            ends = right[i] - i
            # print("a[i]: ", arr[i],"sts, ends: ", sts, ends, "ends*sts: ", ends*sts)
            ans += arr[i] * (sts * ends) 
        return ans % (10**9 + 7)
    
        
        