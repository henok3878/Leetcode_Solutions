class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ans = []
        
        def helper(i,curr_comb,curr_sum):
            if len(curr_comb) == k:
                if curr_sum == n:
                    ans.append(curr_comb[:])
                return
            if(i > 9 or len(curr_comb) > k or curr_sum > n):
                return
            curr_comb.append(i)
            helper(i+1,curr_comb,curr_sum + i)
            curr_comb.pop()
            helper(i+1,curr_comb,curr_sum)
            
        
        helper(1,[],0)
        return ans