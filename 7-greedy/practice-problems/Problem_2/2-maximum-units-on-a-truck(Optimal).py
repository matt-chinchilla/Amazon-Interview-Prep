from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        breakpoint()
        boxTypes.sort(key= lambda x: -x[1])
        capacity=0
        
        for box,unit in boxTypes:
            if truckSize >= box:
                truckSize -= box
                capacity += box*unit
                
            else:
                capacity += truckSize*unit
                break 
            
        return capacity
if __name__ == "__main__":
    s = Solution()
    boxTypes = [[1,3],[2,2],[3,1]]
    truckSize = 4
    print(s.maximumUnits(boxTypes, truckSize))