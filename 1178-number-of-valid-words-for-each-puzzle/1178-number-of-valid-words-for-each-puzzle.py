class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        
        root = TrieNode() 
        def insert(word):
            curr = root 
            for c in word: 
                if c not in curr.kids:
                    curr.kids[c] = TrieNode() 
                curr = curr.kids[c] 
            curr.count += 1 
        
        def search(word,node,first_letter,found):
            ans = node.count if found else 0 
            for c in word:
                ans += search(word,node.kids[c],first_letter,found or c == first_letter) if c in node.kids else 0 
            return ans 
        for word in words:
            insert(set(word))
        return [search(p,root,p[0],False) for p in puzzles]

        
        
        
class TrieNode: 
    def __init__(self):
        self.kids = {} 
        self.count = 0 