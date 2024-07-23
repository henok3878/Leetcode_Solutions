class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums) 
        nums = list(counter.items()) 
        nums.sort(key = lambda x: (x[1],-x[0]))
        ans = []
        for k,v in nums:
            ans += [k] * v
        return ans