from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
            n = len(graph)

            def dfs(num: int, path: List[int]):
                breakpoint()
                if num == n - 1:
                    ans.append(list(path))
                    return
                
                if num > n:
                    return 
                
                for node in graph[num]:
                    path.append(node)
                    dfs(node, path)
                    path.pop()
            
            ans = []
            dfs(0, [0])
            return ans
if __name__ == "__main__":
    s = Solution()
    graph = [[1,2],[3],[3],[]]
    print(s.allPathsSourceTarget(graph))