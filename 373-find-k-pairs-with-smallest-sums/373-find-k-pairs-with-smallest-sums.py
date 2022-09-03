class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i1,i2 = 0,0 
        n1 = len(nums1)
        n2 = len(nums2) 
        
        max_heap = [] 
        visited = set()
        heappush(max_heap,(nums1[0] + nums2[0], 0,0))
        ans = []
        while i1 < n1 and i2 < n2 and max_heap:
            s,i1,i2 = heappop(max_heap) 
            if (i1,i2) in visited:
                continue 
            ans.append([nums1[i1],nums2[i2]])
            visited.add((i1,i2)) 
            if len(ans) == k:
                return ans 
            if i1 + 1 < n1:
                heappush(max_heap,(nums1[i1 + 1] + nums2[0],i1 + 1, 0)) 
            if i2 + 1 < n2:
                heappush(max_heap,(nums1[i1] + nums2[i2 + 1], i1, i2 + 1))
        
        return ans