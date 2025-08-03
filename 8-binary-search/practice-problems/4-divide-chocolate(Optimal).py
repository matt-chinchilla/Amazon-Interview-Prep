from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        left = 1
        right = sum(sweetness) // (k + 1)

        def can_split(mid: int) -> bool:
            breakpoint()
            total, chunks = 0, 0

            for sweet in sweetness:
                total += sweet
                if total >= mid:
                    chunks += 1
                    total = 0
            
            return chunks >= k + 1
        breakpoint()
        while left < right:
            mid = (left + right + 1) // 2
            if can_split(mid):
                left = mid
            else:
                right = mid - 1
        
        return left
    
if __name__ == "__main__":
    s = Solution()
    sweetness = [1,2,3,4,5,6,7,8,9]
    k = 5
    print(s.maximizeSweetness(sweetness,k))