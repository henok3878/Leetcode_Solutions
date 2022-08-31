class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        word_scores = [] 
        for word in words:
            val = 0 
            for c in word:
                idx = ord(c) - ord('a') 
                val += score[idx]
            word_scores.append(val) 
        
        counter = Counter(letters) 
        def is_pos(word):
            count_word = Counter(word) 
            for k,v in count_word.items():
                if v > counter[k]:
                    return False 
            return True 
        def update_counter(word,inc = False):
            count_word = Counter(word) 
            if inc: 
                for k,v in count_word.items():
                    counter[k] += v 
            else:
                for k,v in count_word.items():
                    counter[k] -= v
                
                
        
        def helper(idx):
            if idx == len(words):
                return 0 
            
            select = 0 
            if is_pos(words[idx]):
                update_counter(words[idx])
                select = helper(idx + 1) + word_scores[idx]
                update_counter(words[idx],True)
            skip = helper(idx + 1)
            
            return max(skip,select)
        return helper(0)