class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s) 
        k = len(t) 
        if k > n:
            return "" 
        dict_t = defaultdict(int) 
        for c in t:
            dict_t[c] += 1 
        
        def check(curr):
            for k in dict_t:
                if curr[k] < dict_t[k]:
                    return False 
            return True 
        curr = defaultdict(int) 
        l = 0 
        ans = float('inf')
        st = -1
        for r in range(n):
            curr[s[r]] += 1 
            while l <= r and check(curr):
                # print("l:", l, "r:", r, "s[l:r]", s[l:r + 1])
                curr_l = r - l + 1 
                if curr_l < ans:
                    ans = curr_l 
                    st = l
                curr[s[l]] -= 1 
                l += 1 
        
        if ans == float('inf'):
            return "" 
        return s[st:st + ans]
            
             

        

"""
Chars:  
    - Upper & lower case letters
    - 52 chars in total (26 each) 

len(s), len(t) <= 10**5 


N = len(s)
M = len(t) 

if M > N:
    no way 
else:
    # O(N * 52) 

- each index in s has a potential to be the start of our answer string and we have n such indices 

- for each index in s: #N
    - check if there is a substring starting here that contains t, if so return the len #M 
    
___________________________________________
^***********
 ^***********

if we check for index i, using O(M) time, find a way to check for (i + 1) in O(1) time 

brute force: O(N*M)





"""