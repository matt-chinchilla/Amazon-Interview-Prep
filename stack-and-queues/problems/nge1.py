from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]):
        stack = []
        hashmap = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                hashmap[stack.pop()] = num
            stack.append(num)
            
        return [hashmap.get(i, -1) for i in nums1]      # return i if it is in the hashmap, return -1 else
    
if __name__ == "__main__":
    sol = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    sol.nextGreaterElement(nums1, nums2)