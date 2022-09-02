class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        @cache 
        def helper(rem):
            cost = 0
            #Consider using price only 
            for i,item in enumerate(rem): 
                cost += item * price[i]
                
            #consider special offers 
            for offer in special: 
                using_curr_offer = offer[-1]
                new_rem = []
                for i,item in enumerate(offer[:len(offer) - 1]):
                    if item > rem[i]:
                        using_curr_offer = -1
                        break 
                    new_rem.append(rem[i] - item) 
                if using_curr_offer == -1:
                    continue 
                cost = min(cost, using_curr_offer + helper(tuple(new_rem))) 
            
            return cost 
        
        return helper(tuple(needs))
            