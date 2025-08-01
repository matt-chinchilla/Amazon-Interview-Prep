class Solution:
    def makeGood(self, s: str) -> str:
        res_stack = [s[0]]                  # Stack that is prepopulated by the first letter in the string
        
        for char in s[1:]:
            if res_stack and char.upper() == char and char.lower() == res_stack[-1]:
                res_stack.pop()
            elif res_stack and char.lower() == char and char.upper() == res_stack[-1]:
                res_stack.pop()
            else:
                res_stack.append(char)
        
        return "".join(res_stack)
    
if __name__ == "__main__":
    sol = Solution()
    s = "kkdsFuqUfSDKK"
    print(sol.makeGood(s))
