class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # just find the lexicographically largest substring of size `len(word) - (numFriends - 1)` or less
        if numFriends == 1:
            return word 

        n = len(word)
        mx_ans_len = n - (numFriends - 1)
        chars = sorted(list(word)) # O(n)
        largest = chars[-1] 

        largest_idx = [idx for idx, char in enumerate(word) if char == largest]

        curr = ""
        for leng in range(mx_ans_len):

            if not largest_idx:
                break
                
            curr_best = 'a'
            for idx in largest_idx:
                curr_best = max(curr_best, word[idx])

            curr += curr_best 
            new_largest_idx = []
            for i,idx in enumerate(largest_idx):

                if idx + 1 < n and word[idx] == curr_best: 
                    largest_idx[i] += 1
                    new_largest_idx.append(idx + 1)

            largest_idx = new_largest_idx

        return curr    
