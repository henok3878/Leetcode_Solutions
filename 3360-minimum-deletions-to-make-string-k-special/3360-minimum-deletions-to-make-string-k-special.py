class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freqs = sorted(list(Counter(word).values()))
        ans = float('inf')
        n = len(freqs)
        
        for i in range(n):
            base = freqs[i]
            curr_ans = sum(freqs[:i])
            
            for j in range(i, n):
                if freqs[j] > base + k:
                    curr_ans += freqs[j] - (base + k)
            ans = min(ans, curr_ans) 
        
        return ans