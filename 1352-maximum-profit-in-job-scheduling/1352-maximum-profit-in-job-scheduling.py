class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(st, end, proft) for st, end, proft in zip(startTime, endTime, profit)]
        jobs.sort(key = lambda x: (x[1], x[0]))
        stack = []
        ans = 0
        for i in range(len(jobs)):
            st, end, profit = jobs[i]
            # print("stack: ", stack, "st,end", st, end)
            if len(stack) == 0:
                stack.append((end, profit))
            else:
                best_prev = 0
                l = 0 
                h = len(stack) - 1 
                while l <= h:
                    mid = (l + h) // 2 
                    if stack[mid][0] <= st:
                        best_prev = stack[mid][1] 
                        l = mid + 1 
                    else:
                        h = mid - 1 
                curr_profit = best_prev + profit

                # print("curr_profit: ", curr_profit, "st,end", st, end, "profit[i]:",profit)
                if curr_profit > stack[-1][-1]:
                    stack.append((end, curr_profit)) 
            ans = max(ans, stack[-1][-1])
        return ans
        
"""
given (end_time, i) for each job we have two options:


"""