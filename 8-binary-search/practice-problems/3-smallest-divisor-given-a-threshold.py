from typing import List
from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        breakpoint()
        if len(nums) > threshold:
            return -1
        
        def check(k):
            breakpoint()
            divisor = 0
            for n in nums:
                divisor += ceil(n/k)
                
            return divisor <= threshold
        
        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
    
if __name__ == "__main__":
    s = Solution()
    nums = [1,2,5,9]
    threshold = 6
    print(s.smallestDivisor(nums, threshold))