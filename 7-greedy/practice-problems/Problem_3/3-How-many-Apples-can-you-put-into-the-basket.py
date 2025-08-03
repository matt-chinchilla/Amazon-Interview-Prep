from typing import List
import heapq

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        ans = 0
        curr_weight = 0
        weight.sort()
        
        for w in weight:
            curr_weight += w
            if curr_weight > 5000:
                break
            ans += 1
        
        return ans
    
if __name__ == "__main__":
    s = Solution()
    weight = [100,200,150,1000]
    print(s.maxNumberOfApples(weight))