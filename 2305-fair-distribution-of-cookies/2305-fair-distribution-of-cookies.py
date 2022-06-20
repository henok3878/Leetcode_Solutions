class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childs = [0] * k 
        min_sofar = 10**20
        def helper(i,childs):
            nonlocal min_sofar
            
            if max(childs) > min_sofar:
                return min_sofar
            if i == len(cookies):
                return max(childs)
            else:
                for c in range(k):
                    childs[c] += cookies[i]
                    min_sofar = helper(i + 1, childs)
                    childs[c] -= cookies[i]
                return min_sofar
        
        return helper(0,childs)
        