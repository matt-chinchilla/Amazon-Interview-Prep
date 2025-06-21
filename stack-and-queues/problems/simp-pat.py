# '.' == active index in stack
# '..' == stack.pop()
# '/' == '//' == '///' || Skip c when stack[-1] == c
# '...' and '....' == (char)
from typing import List

class Solution:
    def simplifyPathTrashSolution(self, path: str):
        # def remove_doubles(word: str):
        #     letters = []
        
        #     for c in word:
        #         if letters and letters[-1] == c and c == '/':
        #             letters.pop()
        #         else:
        #             letters.append(c)
                    
        #     return "".join(letters)
        # path = remove_doubles(path)
        parts = path.split('/')
        
        directory: List = []
        
        keyword_map = {
            '.': lambda: None,
            '..': lambda: directory.pop() if directory else None
        }
        for c in parts:
            if c in keyword_map:
                keyword_map[c]()
            elif c:
                directory.append(c)
        return '/' + '/'.join(directory)
    
    def simplifyPath(self, path: str) -> str:
        stack = []
        for token in path.split('/'):
            if token == '' or token == '.':
                continue
            elif token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)

if __name__ == "__main__":
    path = "/.../a/../b/c/../d/./"
    sol = Solution()
    print(sol.simplifyPath(path))

