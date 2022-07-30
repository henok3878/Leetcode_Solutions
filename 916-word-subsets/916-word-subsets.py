class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res = [] 
        
        letters = [0] * 26 
        for word in words2:
            
            temp = [0] * 26 
            for char in word: 
                temp[ord(char) - ord('a')] += 1 
            
            for i in range(26): 
                letters[i] = max(temp[i], letters[i]) 
        
        for word in words1: 
            counter = Counter(word) 
            valid = True 
            for i in range(26):
                c = chr(i + ord('a')) 
                if letters[i] == 0:
                    continue 
                elif c not in counter or counter[c] < letters[i]: 
                    valid = False 
                    break 
            if valid: 
                res.append(word)
                
        return res
                
        
                
                
            