class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        
        def match(word):
            mapping = {} 
            used = set()
            for i,w in enumerate(word):
                if w in mapping: 
                    if pattern[i] != mapping[w]:
                        return False 
                elif pattern[i] in used:
                    return False
                else: 
                    mapping[w] = pattern[i] 
                    used.add(pattern[i])
            
            return True 
            
            
            
        res = [] 
        for word in words: 
            if match(word): 
                res.append(word)
        
        return res 
        