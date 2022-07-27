class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.num_to_index = defaultdict(list) 
        for i, num in enumerate(nums):
            self.num_to_index[num].append(i)

    def pick(self, target: int) -> int:
        leng = len(self.num_to_index[target])
        idx = randint(0,leng-1)
        return self.num_to_index[target][idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)