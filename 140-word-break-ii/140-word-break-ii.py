class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        root = TrieNode()
        
        def insert(word):
            curr = root 
            for char in word:
                idx = ord(char) - ord('a') 
                if curr.kids[idx] is None:
                    curr.kids[idx] = TrieNode() 
                curr = curr.kids[idx] 
            curr.isWord = True 
            
        def segment(node,path,curr,i):
            #print("E",path,curr,i)
            if not node:
                return 
            if i == len(s):
                #print("I",path, curr,i)
                res.append(" ".join(path))
                return 
            idx = ord(s[i]) - ord('a') 
            if node.kids[idx] is None:
                return 
            curr.append(s[i])
            node = node.kids[idx]
            if node.isWord:
                path.append("".join(curr))
                segment(root,path,[],i + 1)
                path.pop()
            if i + 1 < len(s):
                segment(node,path,curr, i + 1)
        
        for word in wordDict:
            insert(word) 
        
        res = []
        segment(root,[],[],0)
        return res 
    
        
class TrieNode:
    def __init__(self):
        self.kids = [None] * 26 
        self.isWord = False 