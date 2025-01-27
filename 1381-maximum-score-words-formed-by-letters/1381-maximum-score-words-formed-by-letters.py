class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        freqs = Counter(letters)
        ans = 0
        for mask in range(1 << n):
            used = Counter() 
            res = 0
            pos = True 
            for i in range(n):
                if((mask >> i) & 1):
                    word = words[i] 
                    for ch in word:
                        if(used[ch] + 1 > freqs[ch]):
                            pos = False 
                            break
                        else:
                            res += score[ord(ch) - ord('a')] 
                            used[ch] += 1 
                    if not pos:
                        break 
            if pos:
                ans = max(ans, res) 
        return ans 