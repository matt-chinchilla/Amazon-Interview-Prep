from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]):
        n = len(arr)/2
        
        count = sorted([count for count in Counter(arr).values()], reverse=True)
        i = 0
        while n:
            if count[-1] > n:
                break
            n -= count[-1]
            count.pop()
            
        return len(count)
        
if __name__ == "__main__":
    s = Solution()
    arr = [3,3,3,3,2,2,5,5,5,7]
    print(s.minSetSize(arr))