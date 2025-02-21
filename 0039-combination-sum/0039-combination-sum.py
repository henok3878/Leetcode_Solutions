class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
        ans = []
        n = len(candidates)
        def helper(i, curr, curr_sum):
            if (curr_sum == target):
                ans.append(curr[:]) 
            for j in range(i,n):
                curr_option = candidates[j]
                if(curr_sum + curr_option <= target):
                    curr.append(curr_option) 
                    helper(j,curr, curr_sum + curr_option)
                    curr.pop() 

        helper(0, [], 0) 
        return ans 