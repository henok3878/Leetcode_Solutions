class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        intervals = [ abs(i - j) for i,j in zip(nums1,nums2)] 
        MAX = 10**5 + 1
        counter = [0] * (MAX+ 1)
        ops = k1 + k2 
        for interval in intervals:
            counter[interval] += 1 
        for i in range(MAX,0,-1):
            if ops >= counter[i]:
                ops -= counter[i]
                counter[i - 1] += counter[i]
                counter[i] = 0 
            elif ops == 0:
                break 
            else:
                counter[i - 1] += ops 
                counter[i] -= ops 
                ops = 0
        
        ans = 0 
        for i,v in enumerate(counter):
            ans += (i ** 2) * v
            
        return ans 
