class WordFilter:
    
    #O(N * K^2)
    def __init__(self, words: List[str]):
        self.root = TrieNode() 
        for i,word in enumerate(words):
            for j in range(len(word)-1,-1,-1):
                suf_word = word[j:len(word)] + '-' + word 
                self.__insert(i,suf_word) 
    
    #O(len(word))
    def __insert(self,i, word):
        curr = self.root 
        for char in word: 
            if char not in curr.kids:
                curr.kids[char] = TrieNode() 
            curr = curr.kids[char]
            curr.idx = i
    #O(len(word))
    def __find(self, word):
        curr = self.root 
        for char in word:
            if char not in curr.kids:
                return -1 
            curr = curr.kids[char] 
        return curr.idx 
    #O(len(word) * Q)
    def f(self, pref: str, suff: str) -> int:
        return self.__find(suff + "-" + pref)
        
class TrieNode:
    def __init__(self):
        self.kids = {}
        self.idx = -1 

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)