class WordFilter:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.words = words 
        for i,word in enumerate(words):
            self.__insert(i,word)
    
    # O(len(word))
    def __insert(self,i, word):
        curr = self.root 
        for char in word:
            idx = ord(char) - ord('a') 
            if curr.kids[idx] is None:
                curr.kids[idx] = TrieNode() 
            curr = curr.kids[idx] 
        curr.isWord = True 
        curr.idx = i
        
    # O(len(prefix)) + O(x^26): x = 7 - len(prefix)
    @cache 
    def __find_word_with_prefix(self, prefix):
        res = []
        curr = self.root 
        for char in prefix:
            idx = ord(char) - ord('a')
            if curr.kids[idx] is None:
                return [] 
            curr = curr.kids[idx]
        stack = [curr]
        while stack: 
            curr = stack.pop()
            if curr is None:
                continue 
            if curr.isWord:
                res.append(curr.idx) 
            for i in curr.kids:
                stack.append(curr.kids[i])
        return res 
    
    def f(self, pref: str, suff: str) -> int:
        words_with_pref = self.__find_word_with_prefix(pref) 
        # print("idx", words_with_pref)
        ans = -1 
        for idx in words_with_pref:
            if self.is_suffix_in_word(self.words[idx], suff):
                ans = max(ans,idx)
        return ans 
    
    #O(7)
    def is_suffix_in_word(self,word, suffix):
        r_w,r_s = len(word) - 1, len(suffix) - 1 
        while r_s >= 0 and r_w >= 0:
            if suffix[r_s] == word[r_w]:
                r_s -= 1 
                r_w -= 1 
            else:
                return False 
        return r_s < 0
    
class TrieNode:
    def __init__(self):
        self.kids = defaultdict(lambda: None)
        self.isWord = False 
        self.idx = -1 
    
    
    
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

