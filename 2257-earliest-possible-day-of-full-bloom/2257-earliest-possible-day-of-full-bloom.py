class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plants = list(zip(growTime, plantTime))
        plants.sort(reverse = True) 
        time = 0
        ans = 0
        for (grow, plant) in plants:
            curr = time + plant + grow 
            ans = max(curr, ans)
            time += plant 
        return ans 