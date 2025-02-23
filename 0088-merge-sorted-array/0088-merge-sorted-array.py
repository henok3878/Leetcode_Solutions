class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p2 = 0
        for i in range(n + m):
            if i >= m:
                nums1[i] = nums2[p2] 
                p2 += 1 
            elif p2 < n and  nums1[i] > nums2[p2]:
                nums1[i], nums2[p2] = nums2[p2], nums1[i] 
                temp = p2 
                while temp + 1 < n and nums2[temp] > nums2[temp + 1]:
                    nums2[temp], nums2[temp + 1] = nums2[temp + 1], nums2[temp] 
                    temp += 1 
            # print(nums1, nums2)

     