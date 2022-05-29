class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = []
        
        for word in words:
            mask = 0
            for i in range(len(word)):
                idx = ord(word[i]) - ord('a')
                mask = mask | (1 << idx)
            masks.append(mask)
            
        ans = 0
        
        for i,w1 in enumerate(words):
            for j,w2 in enumerate(words):
                if masks[i] & masks[j] == 0:
                    ans = max(ans,len(w1) * len(w2))
        
        return ans