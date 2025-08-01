from typing import List
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = sticks
        heapq.heapify(min_heap)
        ans = 0
        
        while len(min_heap) > 1:
            new_stick = heapq.heappop(min_heap) + heapq.heappop(min_heap)
            ans += new_stick
            heapq.heappush(min_heap, new_stick)

        return ans
if __name__ == "__main__":
    sol = Solution()
    sticks = [1,8,3,5]
    print(sol.connectSticks(sticks))