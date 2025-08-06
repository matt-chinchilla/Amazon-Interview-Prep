from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = [['a','b','c'],           # map[0]→ 2
               ['d','e','f'],           # map[1]→ 3
               ['g','h','i'],           # map[2]→ 4
               ['j','k','l'],           # map[3]→ 5
               ['m','n','o'],           # map[4]→ 6
               ['p','q','r','s'],       # map[5]→ 7
               ['t','u','v'],           # map[6]→ 8
               ['w','x','y','z']]       # map[7]→ 9
        def backtrack(curr, i):
            breakpoint()
            if len(curr) == len(digits):
                ans.append(curr[:])
                return
            
            else:
                for letter in map[int(digits[i]) - 2]:  # For each letter associated with a digit
                    backtrack(curr + letter, i + 1)
                    
        ans = []
        if digits:
            backtrack("", 0)
        return ans
    
if __name__ == "__main__":
    s = Solution()
    digits = "23"
    print(s.letterCombinations(digits))