from sortedcontainers import SortedList
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        MAX = 10**10
        left = [MAX]
        for i in range(1,n):
            left.append(min(nums[i-1],left[i-1]))
            
        right = []
        sl = SortedList()
        for num in nums[::-1]:
            idx = sl.bisect_left(num)
            if idx - 1 >= 0:
                right.append(sl[idx-1])
            else:
                right.append(MAX)
            sl.add(num)
        right.reverse()
        #print(left)
        #print(right)
        for l,i,r in zip(left,nums,right):
            if(l < r < i):
                return True
        return False
        """
        [5,3,1,4,2,3]
         4  2  M 2 M
        
        
        How to find the largest element to the right which is still less than me 
        """
        
        
        
        
        