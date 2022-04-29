class Trie:

    def __init__(self):
        self.root = Node()
        
        
    def insert(self, word: str) -> None:
        temp = self.root
        for c in word:
            if(temp.childs[c] == None):
                temp.childs[c] = Node()
            temp = temp.childs[c]
        temp.is_word = True
            
    
    def search(self, word: str) -> bool:
        
        temp = self.root
        for c in word:
            if(temp.childs[c] == None):
                return False
            temp = temp.childs[c]
        return temp.is_word == True

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for c in prefix:
            if(temp.childs[c] == None):
                return False
            temp = temp.childs[c]
        return True
    
class Node:
    def __init__(self):
        self.childs = defaultdict(lambda:None)
        self.is_word = False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)