class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefix_sum = 0
        for i in range(k):
            prefix_sum += cardPoints[i]
        
        suffix_sum = 0
        ans = prefix_sum
        for i in range(k-1,-1,-1):
            suffix_sum += cardPoints[n - k + i]
            prefix_sum -= cardPoints[i]
            ans = max(ans,prefix_sum + suffix_sum)
        return ans