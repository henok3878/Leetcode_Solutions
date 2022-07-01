class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        startWordsSorted = [tuple(sorted(x)) for x in startWords]
        starts = set(startWordsSorted)
        ans = 0
        for word in targetWords:
            for i in range(len(word)):
                word = sorted(word)
                temp = word[:i] + word[i + 1:]
                if tuple(temp) in starts:
                    ans += 1
                    break
        
        return ans
                