class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_elem = max(nums)
        counter = Counter(nums)
        aggregate = [0] * (max_elem + 1)
        for i in range(max_elem + 1):
            aggregate[i] = counter[i] * i 
        
        for i in range(2,max_elem + 1):        
            aggregate[i] = max(aggregate[i] + aggregate[i - 2], aggregate[i-1])
        
        return max(aggregate)
        
        