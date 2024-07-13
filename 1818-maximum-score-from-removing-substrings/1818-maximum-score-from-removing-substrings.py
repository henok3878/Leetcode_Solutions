class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(input: str, target_pair: str) -> str:
            stack = []
            for char in input:
                if char == target_pair[1] and stack and stack[-1] == target_pair[0]:
                    stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        
        total_score = 0
        high_priority_pair, low_priority_pair = ("ab", "ba") if x > y else ("ba", "ab")
        
        s1 = remove_substring(s, high_priority_pair)
        total_score += (len(s) - len(s1)) // 2 * max(x, y)
        
        s2 = remove_substring(s1, low_priority_pair)
        total_score += (len(s1) - len(s2)) // 2 * min(x, y)

        return total_score