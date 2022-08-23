class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        root = TrieNode() 
        
        def insert(word):
            curr = root 
            for char in word:
                idx = ord(char) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode() 
                curr = curr.children[idx] 
            curr.isEnd = True 
            
        def find(word):
            curr = root 
            curr_word = []
            for char in word: 
                if curr.isEnd: 
                    return "".join(curr_word)
                idx = ord(char) - ord('a') 
                if curr.children[idx] is None:
                    return word
                curr_word.append(char)
                curr = curr.children[idx] 
            return word 
        
        ans = []
        
        for word in dictionary:
            insert(word)
        
        for word in sentence.split():
            ans.append(find(word))
        
        return " ".join(ans)
                
        
        
class TrieNode: 
    def __init__(self): 
        self.children = [None] * 26 
        self.isEnd = False 