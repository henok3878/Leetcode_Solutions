class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(st, end, proft) for st, end, proft in zip(startTime, endTime, profit)]
        jobs.sort() 

        def find_next(i):
            st,end, _ = jobs[i]
            l = i + 1
            h = len(jobs) - 1 
            nxt = len(jobs)
            while l <= h: 
                mid = (l + h) // 2 
                if jobs[mid][0] >= end:
                    nxt = mid 
                    h = mid - 1 
                else:
                    l = mid + 1 
            return nxt 

        @cache 
        def helper(i):
            if i >= len(jobs):
                return 0 
            nxt = find_next(i) 
            skip = helper(i + 1) 
            choose = helper(nxt) + jobs[i][-1] 

            return max(skip, choose) 
        
        return helper(0)
