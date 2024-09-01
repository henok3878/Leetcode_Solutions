class Node:
    def __init__(self,):
        self.kids = [None] * 26 
        self.word = False 

class WordDictionary:

    def __init__(self):
        self.trie = Node() 

    def addWord(self, word: str) -> None:
        temp = self.trie 
        for c in word:
            idx = ord(c) - ord('a') 
            if temp.kids[idx] is None:
                temp.kids[idx] = Node()
            temp = temp.kids[idx]  
        temp.word = True    

    def search(self, word: str) -> bool:
        n = len(word)
        def helper(idx, node):
            if (idx == n):
                return node and (node.word) 

            c = word[idx]
            if c == '.':
                ans = False
                for ii in range(26):
                    if node.kids[ii] is None:
                        continue 
                    ans = ans or helper(idx + 1, node.kids[ii])
                return ans
            else:
                k = ord(c) - ord('a')
                if node.kids[k] is None:
                    return False 
                return helper(idx + 1, node.kids[k])

        temp = self.trie 
        return helper(0, temp)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)