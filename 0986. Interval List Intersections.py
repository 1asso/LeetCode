class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l, r = 0, 0
        res = []
        while l < len(firstList) and r < len(secondList):
            intersection = [max(firstList[l][0], secondList[r][0]), 
                            min(firstList[l][1], secondList[r][1])]
            if intersection[1] >= intersection[0]:
                res.append(intersection)
            if firstList[l][1] < secondList[r][1]:
                l += 1
            else:
                r += 1
        return res