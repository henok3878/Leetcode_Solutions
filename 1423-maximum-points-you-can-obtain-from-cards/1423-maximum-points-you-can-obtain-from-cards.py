class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
            
        suffix = [0] * ( k + 1)
        for i in range(n-1,n-k-1, -1):
            suffix[n-i] = suffix[n-i-1] + cardPoints[i]
        suffix.reverse()
        ans = -1
        prefix = 0
        for i in range(min(k + 1,n)):
            ans = max(ans,suffix[i] + prefix)
            prefix += cardPoints[i]
        return ans