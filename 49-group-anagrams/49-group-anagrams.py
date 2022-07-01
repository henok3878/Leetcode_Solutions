class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1 
            maps[tuple(counter)].append(s)
            
        return maps.values()
        