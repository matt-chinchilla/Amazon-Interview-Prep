from typing import List
from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if maze[entrance[0]][entrance[1]] == '+':
            return -1
        
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols and maze[r][c] == '.'
       # breakpoint()
        # Inits
        rows = len(maze)
        cols = len(maze[0])
        directions = [
            ('right',  0,  1),
            ('down',   1,  0),
            ('left',   0, -1),
            ('up',    -1,  0),
        ]
        queue = deque([(entrance[0], entrance[1], 0)])
        seen = {(entrance[0], entrance[1])}
        
        while queue:
            r, c, steps = queue.popleft()
            #current_coordinates = (r,c)
            
            if (r == 0 or r == rows-1 or c == 0 or c == cols-1) \
                and (r, c) != (entrance[0], entrance[1]):
                    return steps
                
            for name, dr, dc in directions:
                next_row, next_col = r + dr, c + dc
                if valid(next_row, next_col):
                    if maze[next_row][next_col] == '.':
                        if (next_row, next_col) not in seen:
                            seen.add((next_row, next_col))
                            queue.append((next_row, next_col, steps + 1))
                
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    maze = [["+",".","+","+","+","+","+"],
            ["+",".","+",".",".",".","+"],
            ["+",".","+",".","+",".","+"],
            ["+",".",".",".","+",".","+"],
            ["+","+","+","+","+",".","+"]]
    entrance = [0,1]
    print(sol.nearestExit(maze, entrance))