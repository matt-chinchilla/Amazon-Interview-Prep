class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {'(':')', '{':'}', '[':']'}
        
        breakpoint()
        for c in s:
            if c in matching:                    # If there is an opening bracket  "(, {, [ " // If c is a valid key
                stack.append(c)
            else:   
                if not stack:                    # If the stack is empty (nothing to match with)
                    return False                 # Already know the string is invalid
            
                previous_opening = stack.pop()            # Most recently-appearing opening bracket
                if matching[previous_opening] != c:
                    return False
        breakpoint()
        return not stack                            # Return True if the stack is empty
    
if __name__ == "__main__":
    str = "{([]){}}"
    sol = Solution()
    print(sol.isValid(str))