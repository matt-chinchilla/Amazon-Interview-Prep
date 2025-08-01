from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int):
        def distance(points):
            breakpoint()
            coord_distance = []
            for i in points:
                dist = (i[0]**2 + i[1]**2)**0.5
                coord_distance.append((tuple(i), dist)) 
            return coord_distance

        heap = []
        distances = distance(points)
        breakpoint()
        for coord, val in distances:
            heapq.heappush(heap, (-val, coord))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [shortest[1] for shortest in heap]
    
if __name__ == "__main__":
    sol = Solution()
    points = [[2,2],[2,2],[3,3],[2,-2],[1,1]]
    k = 4
    print(sol.kClosest(points, k))