class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = [] 
        curr = []
        curr_cnt = 0
        def justify(curr, curr_cnt, last = False):
            justified = ""
            if last:
                justified = " ".join(curr) 
            else:
                spaces = maxWidth - curr_cnt 
                div_spaces = spaces 
                rem_spaces = 0 
                if len(curr) > 1:
                    div_spaces = spaces // (len(curr) - 1) 
                    rem_spaces = spaces % (len(curr) - 1) 
                for i in range(len(curr) - 1):
                    word = curr[i]
                    justified += word 
                    justified += " " * div_spaces 
                    if rem_spaces:
                        justified += " " 
                        rem_spaces -= 1 
                justified += curr[-1] 
            justified += (" ") * (maxWidth - len(justified)) 
            return justified 

        for word in words:
            l = len(word)
            spaces = max(0, len(curr))
            if curr_cnt + l + spaces > maxWidth:
                ans.append(justify(curr, curr_cnt))  
                curr_cnt = len(word) 
                curr  = [word] 
            else:
                curr.append(word) 
                curr_cnt += len(word) 
        ans.append(justify(curr, curr_cnt, last = True ))
        return ans 