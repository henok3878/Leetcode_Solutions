class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        # just find the lexicographically largest substring of size len(word) - (numFriends - 1)
        if numFriends == 1:
            return word 

        n = len(word)
        mx_ans_len = n - (numFriends - 1)
        chars = sorted(list(word)) # O(n)
        largest = chars[-1] 

        largest_idx = [idx for idx, char in enumerate(word) if char == largest]

        curr = ""
        for leng in range(mx_ans_len):
            done = all(idx == -1 for idx in largest_idx)

            if done:
                break
                
            curr_best = 'a'
            for idx in largest_idx:
                if idx == -1:
                    continue 
                curr_best = max(curr_best, word[idx])

            curr += curr_best 
            for i,idx in enumerate(largest_idx):
                if idx == -1:
                    continue 
                elif word[idx] == curr_best: 
                    largest_idx[i] += 1
                    if largest_idx[i] == n:
                        largest_idx[i] = -1
                else:
                    largest_idx[i] = -1
        return curr    
