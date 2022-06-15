class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sts = set(words)
        words.sort(key = lambda x : len(x))
        #print(words)
        ans = 1
        count = defaultdict(lambda:1)
        for word in words:
            for i in range(len(word) + 1):
                for c in range(26):
                    ch = chr(c + 97)
                    temp = word[:i] + ch + word[i:]
                    if temp in sts:
                        #print(word,temp)
                        count[temp] = max(count[temp],count[word] + 1)
                        ans = max(ans,count[temp])
                        
        return ans