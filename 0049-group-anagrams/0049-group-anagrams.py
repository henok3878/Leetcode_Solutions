class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def hash(word):
            return "".join(sorted(word)) 
        
        anagrams = {} 
        for word in strs:
            key = hash(word) 
            if key in anagrams:
                anagrams[key].append(word) 
            else:
                anagrams[key] = [word] 
        
        return list(anagrams.values()) 

