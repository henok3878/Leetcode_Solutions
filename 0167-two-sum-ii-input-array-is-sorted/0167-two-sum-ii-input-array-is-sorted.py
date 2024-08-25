class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        idx1 = 0 
        idx2 = n - 1

        while(idx1 < idx2):
            val = numbers[idx1] + numbers[idx2] 
            if(val > target):
                idx2 -= 1 
            elif val < target: 
                idx1 += 1 
            else:
                return [idx1+1, idx2+1] 
