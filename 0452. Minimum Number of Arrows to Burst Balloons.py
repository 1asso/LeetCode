class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        res = 1
        cur = points[0]
        for p in points:
            if p[0] > cur[1]:
                res += 1
                cur = p
        return res
        
        
OR:

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:
                res += 1
            else:
                points[i][1] = min(points[i][1], points[i-1][1])
        return res
