class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:     
        i = 0 
        n = len(s)
        res = []
        idxs = set(indices)
        while i < n:
            found = False
            for j,idx in enumerate(indices):
                if idx == i and idx + len(sources[j]) <= n:
                    temp = s[idx: idx + len(sources[j])]
                    if temp == sources[j]:
                        res.append(targets[j])
                        i += len(sources[j])
                        found = True 
                        break
            if not found:
                res.append(s[i])
                i += 1      
        return "".join(res)