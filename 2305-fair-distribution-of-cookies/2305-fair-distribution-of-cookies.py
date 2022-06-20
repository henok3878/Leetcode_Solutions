class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childs = [0] * k 
        min_sofar = 10**20
        def helper(i,childs):
            nonlocal min_sofar
            max_child = max(childs)
            if max_child > min_sofar:
                return min_sofar
            if i == len(cookies):
                return max_child
            else:
                for c in range(min(i + 1, k)):
                    childs[c] += cookies[i]
                    min_sofar = helper(i + 1, childs)
                    childs[c] -= cookies[i]
                return min_sofar
        
        return helper(0,childs)
        