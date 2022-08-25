class WordFilter:
    
    #O(N * K^2)
    def __init__(self, words: List[str]):
        self.root = TrieNode() 
        
        for i,word in enumerate(words):
            suf_word = deque(['{'] + list(word))
            for j in range(len(word)-1,-1,-1):
                suf_word.appendleft(word[j])
                self.__insert(i,suf_word) 
    
    #O(len(word))
    def __insert(self,i, word):
        curr = self.root 
        for char in word: 
            idx = ord(char) - ord('a')
            if not curr.kids[idx]:
                curr.kids[idx] = TrieNode() 
            curr = curr.kids[idx]
            curr.idx = i
    #O(len(word))
    def __find(self, word):
        curr = self.root 
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.kids[idx]:
                return -1 
            curr = curr.kids[idx] 
        return curr.idx 
    #O(len(word) * Q)
    def f(self, pref: str, suff: str) -> int:
        return self.__find(suff + "{" + pref)
        
class TrieNode:
    def __init__(self):
        self.kids = [None] * 27 
        self.idx = -1 

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)