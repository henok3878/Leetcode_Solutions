class TrieNode:
    def __init__(self):
        self.kids = {} 
        self.cnt = 0 


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = TrieNode() 
        for word in strs:
            curr = trie
            for ch in word:
                if ch not in curr.kids:
                    curr.kids[ch] = TrieNode() 
                curr = curr.kids[ch] 
                curr.cnt += 1 
        longest = '' 
        curr = trie 
        cands = strs[0]
        for ch in cands:
            if curr.kids[ch].cnt != len(strs):
                break 
            longest += ch 
            curr = curr.kids[ch]
        return longest 
        
                