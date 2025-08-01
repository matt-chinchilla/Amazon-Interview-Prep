from typing import List
class Solution:
    def kClosest(self, a: List[List[int]], k: int) -> List[List[int]]:
        return sorted(a, key=lambda p: p[0]**2 + p[1]**2)[:k]
    
if __name__ == "__main__":
    sol = Solution()
    points = [[2,2],[2,2],[3,3],[2,-2],[1,1]]
    k = 4
    print(sol.kClosest(points, k))