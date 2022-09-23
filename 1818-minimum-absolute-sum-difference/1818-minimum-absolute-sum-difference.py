class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_sorted = sorted(nums1)
        best = [-1] * len(nums2) 
        for i,num in enumerate(nums2):
            l = bisect_left(nums1_sorted,num)
            if l == len(nums2):
                best[i] = (abs(num - nums1_sorted[l - 1]),abs(num - nums1[i]))
            elif num == nums1_sorted[l] or l == 0:
                best[i] = (abs(num - nums1_sorted[l]), abs(num - nums1[i]))
            else:
                if abs(num - nums1_sorted[l]) >= abs(num - nums1_sorted[l-1]):
                    best[i] = (abs(num - nums1_sorted[l-1]),abs(num - nums1[i]))
                else:
                    best[i] = (abs(num - nums1_sorted[l]), abs(num - nums1[i]))
        total = 0 
        for num1,num2 in zip(nums1,nums2):
            total += abs(num1- num2) 
        best.sort(key = lambda x: abs(x[0]-x[1]), reverse = True)
        total -= best[0][1]
        total += best[0][0]
        # print(best)
        
        return total % (10**9 + 7)
    
                