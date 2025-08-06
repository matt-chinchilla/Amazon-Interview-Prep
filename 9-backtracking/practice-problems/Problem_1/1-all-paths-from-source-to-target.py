from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        call_stack = []            # will hold tuples: (func_name, curr_path, node_index)
        ans = []
        
        def backtrack(curr, i):
            breakpoint()
            
            call_stack.append(('backtrack', curr[:], i))
            print(f"Depth {len(call_stack):2d} | Stack: {call_stack}")
            
            if curr[-1] == len(graph) -1:
                ans.append(curr[:])
                return 

            else:
                for edge in graph[i]:
                    curr.append(edge)
                    backtrack(curr, edge)
                    curr.pop()
                    
            call_stack.pop()
            
        breakpoint()
        ans = []
        backtrack([0], 0)
        return ans
if __name__ == "__main__":
    s = Solution()
    graph = [[1,2],[3],[3],[]]
    print(s.allPathsSourceTarget(graph))