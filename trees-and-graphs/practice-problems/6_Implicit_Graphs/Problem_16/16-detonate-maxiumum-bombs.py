from typing import List
from collections import deque, defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        
        #Graph-build // Says which bombs can reach which based upon their radius as the hypotneuse 
       # breakpoint()
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x_1, y_1, rad1 = bombs[i]
                x_2, y_2, _ = bombs[j]
                
                # Path between bomb radii
                if rad1**2 >= (x_1 - x_2)**2 + (y_1 - y_2)**2:
                    graph[i].append(j)
        
        def bfs(i):# Finds the max number of bombs that can be set-off in sequence            
            #breakpoint()
            queue = deque([i])
            visited = set([i])
            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                        
            return len(visited)
        
        ans = 0
        for i in range(n):
            ans = max(ans, bfs(i))
            
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    print(sol.maximumDetonation(bombs))