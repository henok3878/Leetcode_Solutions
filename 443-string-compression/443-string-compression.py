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
            if count > 1:
                chars[valid] = chars[i]
                valid += 1
                if count < 10:
                    chars[valid] = str(count)
                    valid += 1
                else:
                    count_str = str(count)
                    for dig in count_str:
                        chars[valid] = dig
                        valid += 1 
            else:
                chars[valid] = chars[i]
                valid +=1 
            i += 1 
        return valid 