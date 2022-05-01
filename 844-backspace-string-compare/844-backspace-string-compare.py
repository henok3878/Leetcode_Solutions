class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
  
        def type(s):
            ss = []
            for c in s:
                if c == '#':
                    if(len(ss) > 0):
                        ss.pop()
                else:
                    ss.append(c)
            return "".join(ss)
    
    
        return type(s) == type(t)