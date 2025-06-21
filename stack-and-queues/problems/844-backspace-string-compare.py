from typing import List
from pprint import pprint

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def stackOperations(s: str) -> List:
            stack = []
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack: 
                    stack.pop()
            return stack        
        
        s_stack, t_stack = stackOperations(s), stackOperations(t)
        return s_stack == t_stack
    
if __name__ == "__main__":
    sol = Solution()
    s = 'ab#c'
    t = 'ad#c'
    print(sol.backspaceCompare(s,t))