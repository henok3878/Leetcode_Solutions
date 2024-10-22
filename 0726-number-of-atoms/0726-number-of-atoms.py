class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)] 
        n = len(formula) 
        i = 0 
        curr_el = ''
        while i < n:
            curr = formula[i] 
            if curr == '(':
                if curr_el:
                    stack[-1][curr_el] += 1 
                    curr_el = ""
                stack.append(defaultdict(int)) 
                i += 1
            elif curr == ')':
                if curr_el:
                    stack[-1][curr_el] += 1 
                    curr_el = ""

                curr_dig = 0 
                j = i + 1 
                while j < n and formula[j].isdigit():
                    curr_dig = curr_dig * 10 + int(formula[j]) 
                    j += 1 
                if curr_dig == 0:
                    curr_dig = 1

                i = j
                curr_elems = stack.pop() 
                for elem in curr_elems:
                    curr_cnt = curr_elems[elem] * curr_dig 
                    stack[-1][elem] += (curr_cnt) 
            elif curr.isdigit():
                curr_dig = int(curr)
                j = i + 1
                while j < n and formula[j].isdigit():
                    curr_dig = curr_dig * 10 + int(formula[j]) 
                    j += 1 
                i = j
                stack[-1][curr_el] += curr_dig 
                curr_el = ''
            else:
                if curr.isupper():
                    # start of new 
                    if curr_el:
                        stack[-1][curr_el] += 1 
                    curr_el = curr 
                    i += 1
                else:
                    # lower 
                    curr_el += curr 
                    i += 1 
                # print("stack:", stack)
        if curr_el:
            stack[-1][curr_el] += 1
        ans = []
        for elem, cnt in stack[-1].items():
            curr = f"{elem}"
            if cnt > 1: 
                curr += f"{cnt}" 
            ans.append(curr) 
        ans.sort() 
        return "".join(ans)
                

            
        
                    


            


"""
K4(ON(SO3)2)2
 ^
elements = {}
curr_el = K

if curr_char is num:

openings = 0
K: 4


O: 2, N: 2, S: 4, O: 12  




"""