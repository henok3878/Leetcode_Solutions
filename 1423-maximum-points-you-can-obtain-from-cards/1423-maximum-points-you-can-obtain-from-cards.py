class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefix = [0] * (k + 1)
        for i in range(k):
            prefix[i + 1] = prefix[i] + cardPoints[i]
            
        suffix = [0] * ( k + 1)
        for i in range(n-1,n-k-1, -1):
            suffix[n-i] = suffix[n-i-1] + cardPoints[i]
        suffix.reverse()
        
        # print(prefix)
        # print(suffix)
        # print([(x + y) for x,y in zip(prefix, suffix)])
        ans = -1
        for i in range(k + 1):
            ans = max(ans,suffix[i] + prefix[i])
        return ans