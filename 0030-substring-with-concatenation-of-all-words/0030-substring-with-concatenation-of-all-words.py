class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        word_len = len(words[0])
        window_size = len(words) * word_len
        words_cnt = {}
        ans = []
        for word in words:
            val = hash(word) 
            if val not in words_cnt:
                words_cnt[val] = 0 
            words_cnt[val] += 1 

        def helper(s, st):
            curr_words = {}
            for i in range(st, st + window_size, word_len):
                curr_word = s[i: i + word_len]
                curr_hash = hash(curr_word) 
                if curr_hash not in words_cnt:
                    return False 
                if curr_hash not in curr_words:
                    curr_words[curr_hash] = 0 
                curr_words[curr_hash] += 1 

            return words_cnt == curr_words 
        for st in range(n - window_size + 1):
            if helper(s, st):
                ans.append(st) 
        return ans 

'''
Input: s = "barfoothefoobarman", words = ["foo","bar"]

we know that the concatnated substring is size of 6: 2 * 3 

we can process s using a sliding window of size 6 

Let's solve a subproblem: 
    given a string of s len(words) * len(words[0]), check if it can be made by using those words 



'''