class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pt1 = m - 1
        pt2 = n - 1
        last_used = (n + m - 1); 
        while(last_used >= 0):
            if( (pt1 >= 0 and pt2 < 0) or (pt1 >= 0 and nums1[pt1] >= nums2[pt2])):
                nums1[last_used] = nums1[pt1]
                pt1 -= 1
            else:
                nums1[last_used] = nums2[pt2]
                pt2 -= 1 
            last_used -= 1 
        
         
        '''
        O(n + m)
        
        nums1 = [1, 2, 3, 0, 0, 0] | nums2 = [2, 5, 6] 
                 ^.                           ^
        
        if nums1 ptr value <= nums2 ptr value -> just advance ptr of nums 1 and repeat         
        nums1 = [4, 5, 6] | nums2 = [2, 3, 4]
                 ^                   ^ 
                 2  3                 4
                                     3 4 4 
                                     ^ 
                                     5 
                                     4 4 5
                
              nums1 = 6, 7, 8 | nums2 = 1, 2,3 ,4  
              
                    O(n*M): 
        if nums2 ptr val < nums1 pt val -> 
        '''