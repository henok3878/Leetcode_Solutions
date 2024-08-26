class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = [] 
        curr = []
        chars_cnt = 0
        for word in words:
            if len(curr) + (chars_cnt) + len(word) <= maxWidth:
                curr.append(word)
                chars_cnt += len(word)
            else:
                #distribute the spaces evenly 
                total_space = (maxWidth - chars_cnt)
                if(len(curr) == 1):
                    ans.append(curr[0] + (" ") * total_space)
                else:
                    space = total_space // (len(curr) - 1)
                    reminder = total_space % (len(curr) -1)
                    line = ""
                    k = len(curr)
                    for i,w in enumerate(curr):
                        line += w 
                        if(i + 1 < k):
                            line += (" " * space) 
                            if reminder > 0:
                                line += " " 
                                reminder -= 1 
                    ans.append(line) 
                curr = [word]
                chars_cnt = len(word)
        if curr:
            line = " ".join(curr)
            line += (" ") * (maxWidth - len(line))
            ans.append(line)
                
        return ans 