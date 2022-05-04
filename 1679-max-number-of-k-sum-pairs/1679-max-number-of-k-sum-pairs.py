class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict = collections.defaultdict(int)
        count = 0
        for i,num in enumerate(nums):
            comp = k-num
            if(dict[comp] > 0):
                count += 1
                dict[comp] -= 1
            else:
                dict[num] += 1
        
        return count