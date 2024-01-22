class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        counts = [0] * (len(nums) + 1)
        for num in nums:
            counts[num] += 1 
            if counts[num] == 2:
                ans.append(num) 
        for i in range(1,len(counts)): 
                if counts[i] == 0:
                    ans.append(i)
        return ans 
        