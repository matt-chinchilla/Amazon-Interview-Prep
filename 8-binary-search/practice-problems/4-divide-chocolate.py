from typing import List

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        num_people = k+1
        left = min(sweetness)
        right = sum(sweetness) // num_people
        breakpoint()
        while left < right:
            mid = (left + right + 1) // 2
            curr_sweetness = 0
            people_with_chocolate = 0
            
            for s in sweetness:
                curr_sweetness += s
                
                if curr_sweetness >= mid:
                    people_with_chocolate += 1
                    curr_sweetness = 0
                    
            if people_with_chocolate >= k + 1:
                left = mid
            else:
                right = mid - 1
                
        return right
    
if __name__ == "__main__":
    s = Solution()
    sweetness = [1,2,3,4,5,6,7,8,9]
    k = 5
    print(s.maximizeSweetness(sweetness,k))