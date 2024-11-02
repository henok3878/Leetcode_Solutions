class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        n = len(words) 
        for i in range(n):
            nxt = (i + 1) % n
            if words[i][-1] != words[nxt][0]:
                return False 
        return True 
        

