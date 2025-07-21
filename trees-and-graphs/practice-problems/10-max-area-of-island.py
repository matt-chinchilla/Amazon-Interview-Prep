from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Inits
        m, n = len(grid), len(grid[0])
        seen = set()
        directions = self.getDirections()
        
        # Bounds Checker
        def valid(row, col):
            return 0 <= row < m and 0 <= col <= n and grid[row][col] == 1
        
        # Movement Iterator
        def nextDirections(currentRow, currentCol):
            for moveInX_Axis, moveInY_Axis in directions:
                yield currentRow + moveInX_Axis, currentCol + moveInY_Axis
        
        # Depth-First Search to explore an island we already stumbled upon
        def dfs(row, col):
            area = 1
            for next_row, next_col in nextDirections(row, col):
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    area += dfs(next_row, next_col)
            return area
        
        max_area = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen: #Stumbled across new Island
                    seen.add((row, col))
                    current_area = dfs(row, col)
                    max_area = max(max_area, current_area)
                    
        return max_area
    @staticmethod
    def getDirections():
        return [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
        
if __name__ == "__main__":
    sol = Solution()
    grid = grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                   [0,0,0,0,0,0,0,1,1,1,0,0,0],
                   [0,1,1,0,1,0,0,0,0,0,0,0,0],
                   [0,1,0,0,1,1,0,0,1,0,1,0,0],
                   [0,1,0,0,1,1,0,0,1,1,1,0,0],
                   [0,0,0,0,0,0,0,0,0,0,1,0,0],
                   [0,0,0,0,0,0,0,1,1,1,0,0,0],
                   [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))