from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.keys = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not (key in self.keys):
            self.keys[key] = []
        vals = self.keys[key] 
        vals.append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:
        if key in self.keys:
            idx = bisect_right(self.keys[key], (timestamp, "")) 
            n = len(self.keys[key])
            if idx == n or self.keys[key][idx][0] > timestamp:
                idx -= 1 
            if idx < 0:
                return ""
            return self.keys[key][idx][1]

        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


'''
key1: <timestamp,val1>, <timestamp, val2>, <timestamp,val3>, ....



- Clarifications: 
    - are timestamps increasing order? 


Approach 1
- key: {} # key -> dictionary (map) , {timestamp: val}

- key: [(timestamp, val)]


Implementation:
- keys = {}, keys[key] = list, each list stores (timestam, val) 



'''