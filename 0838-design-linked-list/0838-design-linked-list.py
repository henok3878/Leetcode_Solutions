class Node:
    def __init__(self, val = 0):
        self.val = val 
        self.nxt = None 

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummy_head = Node() 
        self.tail = self.dummy_head 
        

    def get(self, index: int) -> int:
        if (index >= self.size):
            return -1
        temp = self.dummy_head 
        while index >= 0:
            temp = temp.nxt 
            index -= 1
        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val) 
        new_node.nxt = self.dummy_head.nxt 
        self.dummy_head.nxt = new_node 
        self.size += 1
        if(self.size == 1):
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val) 
        self.tail.nxt = new_node 
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if(index > self.size):
            return
        temp = self.dummy_head
        idx = index
        while(index > 0):
            temp = temp.nxt
            index -= 1 

        new_node = Node(val) 
        new_node.nxt = temp.nxt 
        temp.nxt = new_node 
        if(idx == self.size):
            self.tail = new_node
        self.size += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if(index >= self.size):
            return
        idx = index
        temp = self.dummy_head
        while(index > 0):
            temp = temp.nxt 
            index -= 1 
        nxt_nxt = temp.nxt.nxt 
        nxt = temp.nxt # to be deleted 
        temp.nxt = nxt_nxt 
        nxt.nxt = None # detach 
        self.size -= 1
        if(idx == self.size):
            self.tail = temp

    def print(self):
        temp = self.dummy_head 
        print('[', end = ' ')
        temp = temp.nxt 
        while temp:
            print(temp.val, end = ",")
            temp = temp.nxt 
        print("]")
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)