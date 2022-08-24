class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    
        root = TrieNode() 
        def insert(word):
            curr = root 
            for char in word:
                idx = ord(char) - ord('a') 
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode() 
                curr = curr.children[idx] 
            curr.isWord = True 
        
        def find(word,count):
            curr = root
            for i,char in enumerate(word): 
                idx = ord(char) - ord('a') 
                if curr.isWord:
                    if find(word[i:], count + 1):
                        return True 
                if curr.children[idx] is None:
                    return False 
                curr = curr.children[idx]
            return curr.isWord and count + 1 >= 2 
        
        ans = [] 
        for word in words:
            insert(word)         
            
        for word in words:
            if find(word,0):
                ans.append(word)
        return ans
                    
        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26 
        self.isWord = False 