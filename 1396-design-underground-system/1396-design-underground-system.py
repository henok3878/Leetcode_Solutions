class UndergroundSystem:

    def fact(self):
        return (0,0)
    def __init__(self):
        self.check_ins = {} # id -> [st,t]
        self.trips = defaultdict(self.fact)# st_end -> total, count

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        st_station,st_time = self.check_ins[id]
        key = self.getKey(st_station,stationName)
        total,count = self.trips[key]
        self.trips[key] = (total + t - st_time, count + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = self.getKey(startStation,endStation)
        total,count = self.trips[key]
        return total / count
        
    def getKey(self,st,end):
        return st + "_"+end


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)