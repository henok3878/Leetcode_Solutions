class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1 
        p2 = n - 1 
        final_pos = n + m - 1 
        while final_pos >= 0:
            if p1 >= 0 and p2 >= 0:
                if(nums1[p1] >= nums2[p2]):
                    nums1[final_pos] = nums1[p1]
                    p1 -= 1 
                else:
                    nums1[final_pos] = nums2[p2]
                    p2 -= 1 
            elif p1 >= 0:
                nums1[final_pos] = nums1[p1] 
                p1 -= 1 
            else:
                nums1[final_pos] = nums2[p2] 
                p2 -= 1 
            final_pos -= 1 
        