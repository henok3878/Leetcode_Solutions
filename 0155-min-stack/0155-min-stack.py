class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prev_mn = float('inf') if len(self.stack) == 0 else self.stack[-1][1]
        mn = min(val, prev_mn) 
        self.stack.append((val, mn))
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()