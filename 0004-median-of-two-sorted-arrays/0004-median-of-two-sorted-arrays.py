class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        INF = float('inf') 
        n = len(nums1) + len(nums2) 
        half = ceil(n / 2) 
        l = -1 
        r = len(nums1) - 1 
        nums1.append(INF) 
        nums2.append(INF) 
        while l <= r:
            i = (l + r) // 2 
            j = half - 2 - i 
            if j < -1:
                r = i - 1
                continue  
            elif j >= len(nums2)-1:
                l = i + 1 
                continue 
            curr1 = nums1[i] if i != -1 else float('-inf') 
            curr2 = nums2[j] if j != -1 else float('-inf') 
            # print(i,j)
            if curr1 <= nums2[j + 1] and curr2 <= nums1[i + 1]:
                left_end = max(curr1,curr2) 
                if n % 2:
                    return left_end 
                return 0.5*(left_end +(min(nums1[i + 1], nums2[j + 1])))
            elif curr1 > nums2[j + 1]:
                r = i - 1 
            else:
                l = i + 1
        return -1 
            