class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        maps = {"]":"[", ")":"(", "}":"{"}
        for c in s:
            if c in maps.values():
                stk.append(c)
            else:
                comp = maps[c] 
                if not stk or stk[-1] != comp:
                    return False 
                else:
                    stk.pop() 
        return len(stk) == 0 