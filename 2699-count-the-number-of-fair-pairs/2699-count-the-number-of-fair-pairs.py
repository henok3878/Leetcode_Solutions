from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList() 
        ans = 0
        for num in nums:
            mx = upper - num
            mn = lower - num
            cnt_mn = sl.bisect_right(mn-1) 
            cnt_mx = sl.bisect_right(mx) # idx of the next greater elem (cnt of elem <= mx)

            ans += (cnt_mx - cnt_mn)

            sl.add(num)
        return ans 

        """

        0, 1, 7, 4, 4, 5

        nums[i] + nums[j] >= lower 
        nums[i] + nums[j] <= upper 

        nums[i] >= lower - nums[j] 
        nums[i] <= upper - nums[j]

        Mn = lower - nums[j] 
        Mx = upper - nums[j] 

        How many numbers are there <= Mx and < Mn (or <= (Mn - 1))

        and then valid count = count_Mx - count_less_mn

        L = 3 
        U = 6
        """