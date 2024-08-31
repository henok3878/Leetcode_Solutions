class TrieNode:
    def __init__(self):
        self.kids = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
        

    def insert(self, word: str) -> None:
        temp = self.root 
        for c in word:
            idx = ord(c) - ord('a') 
            if temp.kids[idx] is None:
                temp.kids[idx] = TrieNode() 
            temp = temp.kids[idx] 
        temp.end = True 
        

    def search(self, word: str) -> bool:
        temp = self.root 
        for c in word:
            idx = ord(c) - ord('a') 
            if temp.kids[idx] is None:
                return False 
            temp = temp.kids[idx] 
        return temp.end 
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.root 
        for c in prefix:
            idx = ord(c) - ord('a') 
            if temp.kids[idx] is None:
                return False 
            temp = temp.kids[idx] 
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)