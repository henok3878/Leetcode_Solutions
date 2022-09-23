class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums1_sorted = sorted(nums1) 
        total = 0 
        gain = 0 
        for num1,num2 in zip(nums1,nums2):
            l = bisect_left(nums1_sorted,num2) 
            curr = abs(num2-num1)
            if l < n:
                gain = max(gain,curr - abs(num2 - nums1_sorted[l])) 
            if l > 0:
                gain = max(gain, curr -abs(num2 - nums1_sorted[l-1]) ) 
            total += curr
        return (total - gain) % (10**9 + 7)