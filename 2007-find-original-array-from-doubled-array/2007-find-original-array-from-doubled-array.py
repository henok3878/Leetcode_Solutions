class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        counter = defaultdict(int)
        for num in changed:
            counter[num] += 1 

        ans = []
        changed.sort()
        for num in changed:
            if num == 0 and counter[num] > 1:
                counter[num] -= 2 
                ans.append(num)
            elif num != 0 and counter[num] > 0 and counter[num * 2] > 0:
                ans.append(num)
                counter[num] -= 1 
                counter[num * 2] -= 1 
        #print(ans)
        if 2*len(ans) != n:
            return []
        return ans