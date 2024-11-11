class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        mx_num = 10**3 + 5 
        is_prime = [True] * mx_num 
        primes = []
        for i in range(2, mx_num):
            if is_prime[i]:
                primes.append(i)
                j = 2 
                while (i * j) < mx_num:
                    is_prime[i * j] = False 
                    j += 1 
        prev = 0 
        # print(primes)
        for num in nums:
            l = 0 
            r = len(primes) - 1
            best = num
            while l <= r:
                mid = (l + r) // 2 
                if num - primes[mid] > prev:
                    best = primes[mid] 
                    l = mid + 1 
                else:
                    r = mid - 1    
            delta = num - best 
            if delta > prev:
                prev = delta 
                if prev < num < delta:
                    prev = num 
            elif num > prev:
                prev = num 
            else:
                return False 
        return True 
