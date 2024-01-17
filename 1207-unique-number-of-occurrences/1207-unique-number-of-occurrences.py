class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr) 
        countOcc = Counter(count.values())
        for k, v in countOcc.items():
            if v > 1:
                return False 
        return True 