from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()             # queue consists of 
        
        breakpoint()
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:   # When the next num is smaller (violates monotonic non-increasing)
                queue.pop()
            queue.append(i)
            
            if queue[0] + k == i:       # if current element is outside of the window
                queue.popleft()
                
            # Whatever is at the front of the queue is already the largest element // Only want ot add it if we are already at the k-element
            if i >= k-1:
                ans.append(nums[queue[0]])
        breakpoint()
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))