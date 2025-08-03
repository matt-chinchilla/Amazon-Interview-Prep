import bisect
from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        breakpoint()
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            
        ans = []
        
        for query in queries:
            index = bisect.bisect_right(nums, query)
            ans.append(index)
        
        return ans
    
if __name__ == "__main__":
    s = Solution()
    nums = [4,5,2,1]
    queries = [3,10,21]
    print(s.answerQueries(nums, queries))