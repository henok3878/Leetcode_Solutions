class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        
        n = len(s)
        def find_ord(c):
            return ord(c) - ord('a') + 1 
        def init_hash():
            hash_val = 0 
            for i in range(k):
                idx = (n - k + i)
                hash_val = ( hash_val + find_ord(s[idx]) * (pow(power,i,modulo))) % modulo 
            return hash_val 
        
        hash_val = init_hash() 
        best = -1
        if hash_val == hashValue:
            best = n - k 
        pow_k = pow(power,k,modulo)
        for i in range(n-k-1,-1,-1):
            hash_val *= power 
            hash_val = ( hash_val - find_ord(s[i + k])*pow_k) % modulo
            hash_val = (hash_val + find_ord(s[i])) % modulo
            # print(i,hash_val,s[i: i + k])
            if hash_val == hashValue:
                best = i
        return s[best: best + k]