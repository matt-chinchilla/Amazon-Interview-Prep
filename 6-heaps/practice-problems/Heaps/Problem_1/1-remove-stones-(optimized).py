from typing import List
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-x for x in piles]
        heapq.heapify(pq)
        for _ in range(k):
            heapq.heapreplace(pq, pq[0]//2)
        return -sum(pq)
    
if __name__ == "__main__":
    sol = Solution()
    piles = [4,3,6,7]
    k = 3
    print(sol.minStoneSum(piles, k))