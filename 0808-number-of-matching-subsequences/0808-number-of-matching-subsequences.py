class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        nxt = [[] for _ in range(26)] 
        for i in range(n):
            ch = ord(s[i]) - ord('a')
            nxt[ch].append(i) 
        
        def find_nxt_i(ch, i):
            ch = ord(ch) - ord('a')
            low = 0
            high = len(nxt[ch])-1
            best = -1 
            while low <= high:
                mid = (low + high) // 2 
                if nxt[ch][mid] >= i:
                    best = nxt[ch][mid]
                    high = mid - 1 
                else:
                    low = mid + 1 
            return best 
        cnt = 0 
        for word in words:
            valid = True 
            i = 0
            for ch in word:
                ii = find_nxt_i(ch, i) 
                if ii == -1:
                    valid = False 
                    break 
                else:
                    i = ii + 1
            if valid:
                cnt += 1 
        return cnt 
                
        
