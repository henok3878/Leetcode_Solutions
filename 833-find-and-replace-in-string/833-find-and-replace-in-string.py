class Solution:
    # O(n)*O(k) + O(n) = O(n)*O(k)
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        maps = defaultdict(lambda:-1)
        # O(k)*O(n)
        for i,sub_str in enumerate(sources): # O(k)
            if s.find(sub_str,indices[i]) == indices[i]: # O(n)
                maps[indices[i]] = i
                  
        idx = 0
        ans = ""
        while idx < len(s): # O(n)
            if maps[idx] != -1:
                pos = maps[idx]
                ans += targets[pos]
                idx += len(sources[pos])
            else:
                ans += s[idx]
                idx += 1
        return ans