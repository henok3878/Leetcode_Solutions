from random import choice
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.num_idx = {}

    def insert(self, val: int) -> bool:
        if(val in self.num_idx):
            return False 
        else:
            self.num_idx[val] = len(self.nums)
            self.nums.append(val)
            return True
        
    def remove(self, val: int) -> bool:
        if(val in self.num_idx):
            idx = self.num_idx[val] 
            n = len(self.nums) - 1
            self.num_idx[self.nums[-1]] = idx
            del self.num_idx[val]
            self.nums[n],self.nums[idx] = self.nums[idx], self.nums[n] 
          
            self.nums.pop() 
            return True 
        return False 

    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()