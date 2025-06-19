class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        breakpoint()
        for c in s:
            if stack and stack[-1] == c: # If the stack isn't empty AND the top of the stack is equal to c
                stack.pop()
            else:
                stack.append(c)
                
        breakpoint()        
        return "".join(stack)

if __name__== "__main__":
    s = "abbaca"
    sol = Solution()
    print(sol.removeDuplicates(s))