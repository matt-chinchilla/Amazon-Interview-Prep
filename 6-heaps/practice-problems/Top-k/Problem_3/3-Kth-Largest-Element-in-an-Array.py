from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        ok = nums
        poop = [-num for num in ok]
        heapq.heapify(poop)
        
        for _ in range(k-1):
            heapq.heappop(poop)
        
        return -heapq.heappop(poop)
    
if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,5,6,4]
    k = 2
    print(sol.findKthLargest(nums, k))