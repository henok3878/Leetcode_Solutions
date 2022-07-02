class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = defaultdict(list)
        
        for word in words:
            starting_char = word[0]
            buckets[starting_char].append(word)
            
        counter = 0   
        for c in s:
            curr_words = buckets[c]
            buckets[c] = []
            for word in curr_words:
                suffix = word[1:]
                if len(suffix) == 0:
                    counter += 1 
                else:
                    starting_char = suffix[0]
                    buckets[starting_char].append(suffix)
        
        
        return counter 