from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        breakpoint()
        left = 0
        right = len(nums) -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid + 1
                
            else:
                right = mid -1
        return left

if __name__ == "__main__":
    s = Solution()
    nums = [1,3,5,6]
    target = 2
    print(s.searchInsert(nums, target))