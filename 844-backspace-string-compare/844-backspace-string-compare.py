class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = deque()
        ts = deque()
        
        for c in s:
            if c == '#':
                if(len(ss) > 0):
                    ss.pop()
            else:
                ss.append(c)
        
        for c in t:
            if c == '#':
                if(len(ts) > 0):
                    ts.pop()
            else:
                ts.append(c)
    
    
        s = "".join(ss)
        t = "".join(ts)
        return s == t