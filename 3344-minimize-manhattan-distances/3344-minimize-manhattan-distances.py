class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points) 
        def mx_after_removal(idx):
            furthest = [] 
            mx_dist = 0
            a,b = points[0]
            minus_minus = [0, -a -b] # try to keep smaller negative number - a - b 
            plus_minus = [0, a -b] # a-b 
            minus_plus = [0, -a + b] # -a + b 
            plus_plus = [0, a + b] # a + b 

            for i in range(1, n):
                if i == idx:
                    continue
                x,y = points[i]
                # x + y with - a - b
                # x -y with -a + b 
                # y - x with a - b 
                # -x - y with a + b 

                op1 = (x + y) + minus_minus[1]
                op2 = (x - y) + minus_plus[1]
                op3 = (y - x) + plus_minus[1] 
                op4 = -x - y + plus_plus[1] 

                curr_mx = max(op1, op2, op3, op4) 
                if curr_mx > mx_dist:
                    mx_dist = curr_mx 
                    furthest = [i]
                    if curr_mx == op1:
                        furthest.append(minus_minus[0])
                    elif curr_mx == op2:
                        furthest.append(minus_plus[0]) 
                    elif curr_mx == op3:
                        furthest.append(plus_minus[0]) 
                    else:
                        furthest.append(plus_plus[0])

                if -x -y > minus_minus[1]:
                    minus_minus = [i, -x-y] 
                if x - y > plus_minus[1]:
                    plus_minus = [i, x - y] 
                if -x + y > minus_plus[1]:
                    minus_plus = [i, -x + y] 
                if x + y > plus_plus[1]:
                    plus_plus = [i, x + y] 
            # print("furthest:", furthest)
            return furthest, mx_dist


        furthest, mx_dist = mx_after_removal(-1)
        if mx_dist == 0:
            return 0
        # print(furthest, mx_dist)
        point1, point2 = furthest 
        if point1 == 0:
            if point2 == 1:
                points[0], points[-1] = points[-1], points[0] 
                point1 = n - 1 
            else:
                points[0], points[1] = points[1], points[0] 
                point1 = 1 
        
        if point2 == 0:
            if point1 == 1:
                points[0], points[-1] = points[-1], points[0] 
                point2 = n - 1 
            else:
                points[0], points[1] = points[1], points[0] 
                point2 = 1 

        _, dist1 = mx_after_removal(point1)
        _, dist2 = mx_after_removal(point2)

        return min(dist1, dist2)