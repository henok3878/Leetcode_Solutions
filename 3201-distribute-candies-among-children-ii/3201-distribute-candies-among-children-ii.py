class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        limit = min(n, limit)
        ans = 0 
        for c in range(limit + 1):
            rem = n - c 
            if rem > 2*limit:
                continue 
            mx_b = min(rem, limit)
            mn_b = max(0, rem - limit)
            rng_b = mx_b - mn_b + 1
            ans += rng_b
        return ans 