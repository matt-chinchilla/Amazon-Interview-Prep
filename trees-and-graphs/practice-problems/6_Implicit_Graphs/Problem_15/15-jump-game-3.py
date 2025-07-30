from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()   
            if arr[node] == 0:
                return True
            
            indexRight = node + arr[node]
            indexLeft = node - arr[node]
            
            if indexRight not in visited and indexRight < len(arr):
                queue.append(indexRight)
                
            if indexLeft not in visited and indexLeft >= 0:
                queue.append(indexLeft)
                
            visited.add(node)
        return False
    
if __name__ == "__main__":
    sol = Solution()
    arr = [4,2,3,0,3,1,2]
    start = 5
    
    print(sol.canReach(arr, start))