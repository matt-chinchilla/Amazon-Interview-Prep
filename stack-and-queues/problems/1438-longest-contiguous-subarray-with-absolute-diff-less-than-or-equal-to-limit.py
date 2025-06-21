from collections import deque
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increasing = deque()
        decreasing = deque()
        
        left = ans = 0
        breakpoint()
        for right in range(len(nums)):
            # maintain monotonic deques
            while increasing and increasing[-1] > nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1] < nums[right]:
                decreasing.pop()        
                        
            increasing.append(nums[right])
            decreasing.append(nums[right])
            
            while decreasing[0] - increasing[0] > limit:
                if nums[left] == decreasing[0]:
                    decreasing.popleft()
                if nums[left] == increasing[0]:
                    increasing.popleft()
                    
                left += 1
        
            ans = max(ans, right - left + 1)
        breakpoint()
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    nums = [8,2,4,7]
    limit = 4
    sol.longestSubarray(nums, limit)