class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        maps = defaultdict(lambda:-1)
        for i,sub_str in enumerate(sources):
            if s.find(sub_str,indices[i]) == indices[i]:
                maps[indices[i]] = i
                  
        idx = 0
        ans = ""
        while idx < len(s):
            if maps[idx] != -1:
                pos = maps[idx]
                ans += targets[pos]
                idx += len(sources[pos])
            else:
                ans += s[idx]
                idx += 1
        return ans