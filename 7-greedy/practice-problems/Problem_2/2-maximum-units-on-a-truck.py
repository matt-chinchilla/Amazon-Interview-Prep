from typing import List
import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int):
        breakpoint()
        heap = []
        for box in boxTypes:
            heapq.heappush(heap, (-box[1], box[0]))

        ans = 0
        while heap and truckSize > 0:
            weight, num_boxes = heapq.heappop(heap)
            can_grab = min(num_boxes, truckSize)
            ans += can_grab * -weight
            truckSize -= can_grab
        
        return ans
if __name__ == "__main__":
    s = Solution()
    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4
    print(s.maximumUnits(boxTypes, truckSize))