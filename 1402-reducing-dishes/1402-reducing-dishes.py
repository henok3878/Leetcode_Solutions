class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort() 
        
        @cache 
        def helper(i,time):
            if i == len(satisfaction):
                return 0 
            skip = helper(i + 1, time)
            select = helper(i + 1, time + 1) + (satisfaction[i] * time) 
            
            return max(skip,select)
        
        return helper(0,1)