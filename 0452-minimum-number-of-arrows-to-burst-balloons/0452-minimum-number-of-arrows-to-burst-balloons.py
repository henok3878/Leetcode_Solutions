class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort() 
        non_overlapping = [] 
        for x, y in points:
            if non_overlapping and non_overlapping[-1][1] >= x:
                y = min(y, non_overlapping[-1][1])
                non_overlapping.pop()
            non_overlapping.append([x, y]) 
        return len(non_overlapping) 