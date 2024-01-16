class RandomizedSet:

    def __init__(self):
        self.val_idx = {}
        self.vals = [] 

    def insert(self, val: int) -> bool:
        # print(self.val_idx)
        if val in self.val_idx:
            return False 
        else:
            self.val_idx[val] = len(self.vals) 
            self.vals.append(val) 
            return True 
        
    def remove(self, val: int) -> bool:
        if val in self.val_idx:
            idx = self.val_idx[val]
            last_el = self.vals[-1]
            self.vals[-1] = val 
            self.vals[idx] = last_el 
            del self.val_idx[val] 
            if idx != len(self.vals)-1:
                self.val_idx[last_el] = idx 
            self.vals.pop() 
            return True 
        return False 

    def getRandom(self) -> int:
        idx = random.randint(0,len(self.vals)-1) 
        return self.vals[idx]
                                        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()