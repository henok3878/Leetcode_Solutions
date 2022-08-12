class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        """
        [1,2,3]
        length of 1: [1],[2], [3] => total = 1 - 1 + 2 - 2 + 3 - 3 = 0  
        length of 2: [1,2], [2,3] => 1 + 1 = 2 
        length of 3: [1,2,3] => 3 - 1 = 2 
        
        total = 4 
        
        n(n + 1) // 2 
        Brute Force: 
            - generate every subarray: O(N^2) b/c N(N + 1) // 2 subarrays 
            - for each subarray: find its range: O(N) 
            
            total: O(N^3) 
        Segment Tree: 
            - generate every subarray: O(N^2) 
            - for each subarray find min and max: O(LogN) 
            
            total: O(N^2LogN)
        Preprocessing: 
            - generate every subarrya: O(N^2) 
            - find min and max: O(1) 
        """
        n = len(nums) 
        total = 0 
        for i in range(n):
            min_elem = nums[i]
            max_elem = nums[i]
            for j in range(i,n):
                min_elem = min(min_elem,nums[j])
                max_elem = max(max_elem, nums[j])
                total += max_elem - min_elem 
        
        return total 