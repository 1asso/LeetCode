class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        res = 0
        for box in boxTypes:
            if truckSize <= 0:
                return res
            res += min(truckSize, box[0]) * box[1]
            truckSize -= box[0]
        return res
