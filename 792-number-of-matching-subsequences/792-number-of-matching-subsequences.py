class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        def is_subsequence(word):
            last = -1 
            for c in word:
                idx = bisect_right(char_to_indices[c],last)
                if idx >= len(char_to_indices[c]):
                    return False
                else:
                    last = char_to_indices[c][idx]
            return True
        
        char_to_indices = defaultdict(list)
        for i,c in enumerate(s):
            char_to_indices[c].append(i) 
            
        valid = 0 
        for word in words:
            if is_subsequence(word):
                valid += 1 
        return valid 