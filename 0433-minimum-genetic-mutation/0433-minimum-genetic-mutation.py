class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        bank = set(bank) 
    
        q = deque()
        q.append(startGene) 
        visited = set()
        visited.add(startGene)

        step = 0
        while q:

            s = len(q)
            for _ in range(s):
                curr = q.popleft() 
                if curr == endGene:
                    return step 
                nxt = list(curr)

                for i in range(8):
                    t = nxt[i]
                    for ch in ["A", 'C','G','T']:
                        
                        if nxt[i] != ch:
                            nxt[i] = ch 
                            nxt_s = "".join(nxt) 
                            if nxt_s in bank and not (nxt_s in visited):
                                q.append(nxt_s)
                                visited.add(nxt_s) 
                    nxt[i] = t
            step += 1 
        
        return -1
