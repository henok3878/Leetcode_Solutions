class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_copy = []
        for s in strs:
            strs_copy.append(''.join(sorted(s)))
        
        maps = defaultdict(list)
        for i,s in enumerate(strs_copy):
            maps[s].append(strs[i])
            
        return maps.values()
        