class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        startWordsSorted = [tuple(sorted(x)) for x in startWords]
        starts = set(startWordsSorted)
        ans = []
        for word in targetWords:
            for i in range(len(word)):
                word = sorted(word)
                temp = word[:i] + word[i + 1:]
                if tuple(temp) in starts:
                    ans.append(word)
                    break
        
        return len(ans)
                