class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        words = set(bannedWords) 
        cnt = 0 
        for word in message: 
            if word in words:
                cnt += 1
        return cnt >= 2 