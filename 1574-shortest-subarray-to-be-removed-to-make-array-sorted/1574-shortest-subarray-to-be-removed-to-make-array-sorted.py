class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        first, i = 0,1 
        while i < n and arr[i] >= arr[i - 1]:
            i += 1 
        first = i
        if first == n:
            return 0
        last, i = 0, n - 2 
        while i > 0 and arr[i] <= arr[ i + 1]:
            i -= 1 
        last = i 
        
        ans = max(first,n - (last + 1)) 
        
        l = 0 
        cnt = 0
        for i in range(first):
            idx = bisect_left(arr,arr[i],last + 1)
            ans = max(ans, i + 1 + (n - idx))            
        return n - ans
        