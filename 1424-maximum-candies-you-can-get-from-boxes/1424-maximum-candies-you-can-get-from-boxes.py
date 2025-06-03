from heapq import heappop as pop, heappush as push 
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        pq = []
        can_open = set() 

        def get_state(box):
            return -(status[box] + int(box in can_open))

        for box in initialBoxes:
            push(pq,(get_state(box), box)) 
            
        ans = 0
        visited = set()
        while pq: 
            # print(f"pq: {pq}")
            state , curr = pop(pq) 
            state = get_state(curr)  

            if not state:
                continue 
                
            ans += candies[curr]
            visited.add(curr)
            can_open.update(keys[curr])
            
            for box in containedBoxes[curr]:
                push(pq, (get_state(box), box))
                
        return ans  