from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int):
        def distance(points):
            coord_distance = {}
            for i in points:
                dist = (i[0]**2 + i[1]**2)**0.5
                coord_distance.update({tuple(i):dist}) 
            return coord_distance
        
        
        return distance(points)
    
if __name__ == "__main__":
    sol = Solution()
    points = [[1,3],[-2,2]]
    k = 1
    print(sol.kClosest(points, k))
    
# Matthew, you have a hashmap with the coordinate as point[0] and the distance as point[1]
# Just implement a Heap & iterate the 'heappop()' operation for A MIN HEAP YOU FAG where the # times == k and return it as an ARRAY