class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        val1 = list(Counter(word1).values())
        val2 = list(Counter(word2).values())
        val1.sort() 
        val2.sort() 
        return val1 == val2 and set(word1) == set(word2)
        