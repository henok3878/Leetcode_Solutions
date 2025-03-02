class RandomizedSet:

    def __init__(self):
        self.seed = 42 
        self.a = 1103515245
        self.c = 12345
        self.m = 2 ** 31 
        self.map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False 
        self.nums.append(val) 
        self.map[val] = len(self.nums) - 1 
        return True 

    def remove(self, val: int) -> bool:
        if val in self.map:
            idx = self.map[val]
            self.map[self.nums[-1]] = idx
            self.nums[-1], self.nums[idx] = self.nums[idx], self.nums[-1]
            self.nums.pop()  
            self.map.pop(val) 
            return True 
        return False 
     

    def getRandom(self) -> int:
        return self.random()

    def random(self):
        n = len(self.nums)
        self.seed = ((self.a * self.seed) + self.c) % self.m 
        idx = int((self.seed / self.m) * n)
        return self.nums[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()