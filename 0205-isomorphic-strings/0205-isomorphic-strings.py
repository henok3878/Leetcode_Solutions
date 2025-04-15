class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = {} 
        seen = set() 
        for i, ch in enumerate(s):
            ch2 = t[i]
            if ch in mappings:
                if mappings[ch] != ch2:
                    return False 
            else:
                if ch2 in seen:
                    return False 
                seen.add(ch2)
                mappings[ch] = ch2
        return True 