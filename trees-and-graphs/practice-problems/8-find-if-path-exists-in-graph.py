from typing import List
from collections import defaultdict

class Solution:
    def validPath1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        breakpoint()
        graph = defaultdict(list)
        for ui, vi in edges:
            graph[ui].append(vi)
            graph[vi].append(ui)

        if not graph:
            return True
        
        def dfs(node):
            breakpoint()
            if node == destination:
                return True
                
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            return False
          
        seen = {source}
        return dfs(source)
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = [False] * n
        
        def dfs(curr_node):
            if curr_node == destination:
                return True
            seen[curr_node] = True
            for next_node in graph[curr_node]:
                # Only call dfs if not seen
                if not seen[next_node]:
                    if dfs(next_node):
                        return True
            return False

        return dfs(source)
if __name__ == "__main__":
    # Test case
    n1 = 3
    n2 = 6
    edges1 = [[0,1],[1,2],[2,0]]
    edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
    source = 0
    destination1 = 2
    destination2 = 5
    
    solution = Solution()
    result = solution.validPath(n1, edges1, source, destination1)
    print(f"Path exists from {source} to {destination1}: {result}")