class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(magazine) 

        for ch in ransomNote:
            if ch not in counter1 or counter1[ch] == 0:
                return False 
            counter1[ch] -= 1
        
        return True 