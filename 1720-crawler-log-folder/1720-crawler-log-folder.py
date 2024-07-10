class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack_len = 0
        for op in logs:
            if op == './':
                continue 
            elif op == '../':
                if stack_len > 0:
                    stack_len -= 1
            else:
                stack_len += 1  
        return stack_len
                

        
