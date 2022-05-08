# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.curr = -1
        self.list = []
        self.setup(nestedList)
    def setup(self,nlist):     
        for ni in nlist:
            if(ni.isInteger()):
                self.list.append(ni.getInteger())
            else:
                self.setup(ni.getList())
    
    def next(self) -> int:
        self.curr += 1
        nxt = self.list[self.curr]
        return nxt
    
    def hasNext(self) -> bool:
         return self.curr + 1 < len(self.list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())