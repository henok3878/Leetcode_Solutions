class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False 
        self.map[val] = len(self.nums)
        self.nums.append(val) 
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
        return random.choice(self.nums) 

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()