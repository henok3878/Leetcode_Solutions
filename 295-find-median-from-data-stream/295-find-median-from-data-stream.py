class MedianFinder:

    def __init__(self):
        self.min_heap = [] 
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heappush(self.min_heap, -heappushpop(self.max_heap, -num)) 
        if len(self.min_heap) > len(self.max_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def findMedian(self) -> float:
        return (0.5 * (self.min_heap[0] + -self.max_heap[0])) if len(self.min_heap) == len(self.max_heap) else -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()