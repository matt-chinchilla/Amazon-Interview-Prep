from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rows = len(board)
        cols = len(board[0])
        
        for x, y in board:
            
    
if __name__ == "__main__":
    sol = Solution()
    board = [[-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,35,-1,-1,13,-1],
             [-1,-1,-1,-1,-1,-1],
             [-1,15,-1,-1,-1,-1]]
    print(sol.snakesAndLadders(board))