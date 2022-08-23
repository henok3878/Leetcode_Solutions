class Solution:
    def findMaximumXOR(self, nums):
        
        root = TrieNode()
        
        def insert(num):
            curr = root 
            for i in range(31,-1,-1):
                idx = (num >> i & 1) 
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode() 
                curr = curr.children[idx] 
            curr.curr_no = num 
        def find(num):
            curr = root 
            for i in range(31,-1,-1):
                idx = (num >> i & 1) 
                if curr.children[idx ^ 1] is None:
                    curr = curr.children[idx]
                else:
                    curr = curr.children[idx ^ 1] 
            return num ^ curr.curr_no     
        
        for num in nums:
            insert(num) 
        ans = 0 
        for num in nums:
            ans = max(ans, find(num)) 
        
        return ans 
    

class TrieNode:
    def __init__(self):
        self.children = [None] * 2 
        self.curr_no = None 