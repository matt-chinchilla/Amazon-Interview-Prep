from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        breakpoint()
        n = len(board)
        cells = [None] * (n**2 + 1)      # +1 because it starts from position 1
        label = 1
        columns = list(range(0, n))
        
        # 1) Make a new grid of all the coordinates in Boustrophedon order
        for row in range(n-1, -1, -1):   # Starting at the bottom of the board (n-1) → go up 1 row upon completion of the loop (n-1, -1) → stop when the row == -1 == "the top" (n-1, -1, -1)
            for column in columns:
                cells[label] = (row, column)#type:ignore
                label += 1
            columns.reverse()
            
        # 2) Make a list of values correlating to the distances at each respective row, column coordinate
        breakpoint()
        dist = [-1] * (n * n + 1)
        q = deque([1])
        dist[1] = 0 # Starting coordinate
        
        while q:
            curr = q.popleft()
            for next in range(curr + 1, min(curr + 6, n**2) +1): # For each of the next 6 plausible landing-locations after a roll
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1
                               else next)
                if dist[destination] == -1:
                    dist[destination] = dist[curr] + 1
                    q.append(destination)
        breakpoint()
        return dist[n * n]
    
if __name__ == "__main__":
    sol = Solution()
    board = [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]]
    print(sol.snakesAndLadders(board))