from typing import List
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
                
        seen = set()
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        ans = 0
        
        for node in range(n):
            if node not in seen:
                dfs(node)
                ans+=1
                
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    n = 5
    edges = [[0,1],[1,2],[3,4]]
    print(sol.countComponents(n, edges))