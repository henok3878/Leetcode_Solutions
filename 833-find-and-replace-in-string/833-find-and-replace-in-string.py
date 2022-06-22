class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        actual_indices = [-1] * len(sources)
        for i,sub_str in enumerate(sources):
            actual_indices[i] = s.find(sub_str,indices[i]) 
        maps = defaultdict(lambda:-1)
        for i,idx in enumerate(indices):
            maps[idx] = i
        idx = 0
        ans = ""
        while idx < len(s):
            if maps[idx] != -1:
                pos = maps[idx]
                if indices[pos] == actual_indices[pos]:
                    sub_str = sources[pos]
                    ans += targets[pos]
                    idx += len(sub_str)
                else:
                    ans += s[idx]
                    idx += 1
            else:
                ans += s[idx]
                idx += 1
        return ans