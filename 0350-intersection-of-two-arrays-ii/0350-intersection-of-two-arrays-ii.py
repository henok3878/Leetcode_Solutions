class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2) 
       
        ans = []
        for k,v in counter1.items():
            mn = min(v, counter2[k]) 
            if mn > 0:
                ans += [k] * mn 
        return ans 