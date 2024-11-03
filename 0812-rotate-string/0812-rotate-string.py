class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False
        for split in range(len(s)):
            offset = len(s) - (split + 1)
            valid = True
            for i in range(len(s)):
                if s[i] != goal[(i + offset)%len(s)]:
                    valid = False 
                    break 
            if valid:
                return True
        return False
