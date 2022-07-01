class Solution:
    def compress(self, chars: List[str]) -> int:
        valid = 0
        n = len(chars)
        i = 0
        while i < n:
            count = 1 
            while i < n - 1 and chars[i] == chars[i + 1]:
                count += 1 
                i += 1 
            chars[valid] = chars[i]
            valid += 1
            i += 1 
            if count > 1:
                for dig in str(count):
                    chars[valid] = dig
                    valid += 1 
        return valid 