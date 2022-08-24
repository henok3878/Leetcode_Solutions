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
            nonlocal ans 
            curr = root
            for i,char in enumerate(word): 
                idx = ord(char) - ord('a') 
                if curr.isWord:
                    #print(word,word[:i],word[i:]) 
                    if find(word[i:], count + 1):
                        return True 
                if curr.children[idx] is None:
                    return False 
                curr = curr.children[idx]
            #print("end",word, curr.isWord, count + 1)
            res =  curr.isWord and count + 1 >= 2 
            if res:
                ans += 1 
            return res 
        ans = 0
        res = []
        for word in words:
            insert(word)         
            
        for word in words:
            temp = ans 
            find(word, 0)
            if temp + 1 == ans:
                res.append(word) 
        return res 
                    
        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26 
        self.isWord = False 