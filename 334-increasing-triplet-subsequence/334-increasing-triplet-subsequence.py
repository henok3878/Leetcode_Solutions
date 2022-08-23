class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a,b = float('inf') , float('inf') 
        
        for num in nums:
            
            if num  > b:
                return True 
            if num < a:
                a = num 
            if num > a:
                b = min(b,num)
            a = min(a,num)
        
        return False 