from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtrack == found a ")" after a "("
        answer = []
        
        def backtracking(curr_string, left_count, right_count):
            breakpoint()
            if len(curr_string) == 2 * n:
                answer.append("".join(curr_string))
                return
            
            if left_count < n:
                curr_string.append("(")
                backtracking(curr_string, left_count + 1, right_count)
                curr_string.pop()
            if right_count < left_count:
                curr_string.append(")")
                backtracking(curr_string, left_count, right_count + 1)
                curr_string.pop()
                
        backtracking([], 0, 0)
        return answer
    
if __name__ == "__main__":
    s = Solution()
    n = 3
    print(s.generateParenthesis(3))