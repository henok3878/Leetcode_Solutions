from sortedcontainers import SortedList

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sl = SortedList()
        leng = 0
        for num in nums:
            idx = sl.bisect_left(num) 
            if idx < len(sl):
                del sl[idx]
            sl.add(num)
            leng = max(leng, len(sl))
            # print("SL: ", sl)
        return leng
