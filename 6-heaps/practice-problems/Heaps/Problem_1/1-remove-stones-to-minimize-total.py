from typing import List
import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #breakpoint()
        heap = [-pile for pile in piles]
        heapq.heapify(heap)

        for _ in range(k):
            biggest = math.ceil(abs(heapq.heappop(heap)) / 2)
            heapq.heappush(heap, -biggest)
            
        return sum([-num for num in heap])
    
if __name__ == "__main__":
    sol = Solution()
    piles = [4,3,6,7]
    k = 3
    print(sol.minStoneSum(piles, k))