class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = [] 
        self.max_len = max([len(w) for w in words]) 
        self.root = TrieNode() 
        for w in words:
            self.__insert(w) 
        
    def __insert(self,word):
        curr = self.root 
        for c in word[::-1]:
            curr = curr.kids[c]   
        curr.is_word = True 
        
    def query(self, letter: str) -> bool:
        self.stream = [letter] + self.stream 
        if len(self.stream) > self.max_len:
            self.stream.pop()
        curr = self.root 
        for c in self.stream:
            if c not in curr.kids:
                return False 
            curr = curr.kids[c]
            if curr.is_word:
                return True 
        return False 
        
        
class TrieNode:
    def __init__(self):
        self.kids = defaultdict(TrieNode)
        self.is_word = False 

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


"""
BruteForce: N^2 

words = ['abc', 'xyz', 'ya'] 

a -> x -> y -> a

xy
y


"""