class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(s):
            say = []
            i = 0
            while( i < len(s)):
                count = 1 
                while(i < len(s) - 1 and s[i] == s[i + 1]):
                    count += 1 
                    i += 1 
                say.append(str(count) + s[i])
                i += 1 
            
            return "".join(say)
        
        s = '1'
        for i in range(1,n):
            s = say(s)
        
        return s 