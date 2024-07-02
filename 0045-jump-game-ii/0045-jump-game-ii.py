class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # Initialize leaves of the tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Initialize internal nodes of the tree
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = min(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, index, value):
        # Update the value at the index
        pos = self.n + index
        self.tree[pos] = value
        # Propagate the change upwards
        while pos > 1:
            pos //= 2
            self.tree[pos] = min(self.tree[pos * 2], self.tree[pos * 2 + 1])

    def range_min_query(self, left, right):
        # Query the minimum value in the range [left, right)
        min_val = float('inf')
        left += self.n
        right += self.n
        while left < right:
            if left % 2:
                min_val = min(min_val, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                min_val = min(min_val, self.tree[right])
            left //= 2
            right //= 2
        return min_val

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        sg = SegmentTree([float('inf')] * n)
        sg.update(n-1,0)
        for i in range(n -2, -1,-1):
            mn = sg.range_min_query(i + 1, min(n ,i + nums[i] + 1))
            sg.update(i, mn + 1)
        return sg.range_min_query(0,1)


       
    '''
    if it is reachable, we can do that with jumps <= n 
    
    Case where it is reachable:
        - 0 -> n
        - isPos(K): returns true if it is possible to reach the end by using K jumps 
        - if possible with k jumps, try 0 - k 
        - else, try k - n 
        - O(isPos) * log2(n)
        
        ^__________
      ^___________________
      
      [2,3,1,1,4]
      
      [2, 1, 2, 1, 0]
      
      The issue is how do you know the min num between i + 1 and i + a[i] for each i 
      
      for i in range(n-1,-1,-1): // 10**4 
        for j in range(i + 1, i + a[i]): // 1000
    
     N*1000 solution will pass in c++. 
     
    
    '''
            