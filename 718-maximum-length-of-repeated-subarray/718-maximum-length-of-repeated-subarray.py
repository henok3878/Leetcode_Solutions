class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        def helper(nums1, nums2):
            ans = 0
            for i in range(len(nums1) - 1,-1,-1):
                j = 0
                match = 0
                while(i < len(nums1) and j < len(nums2)):
                    if nums1[i] == nums2[j]:
                        match += 1
                    else: 
                        match = 0
                    i += 1
                    j += 1
                    ans = max(ans,match)
                
            return ans
        
        first = helper(nums1,nums2)
        return max(helper(nums2,nums1),first)