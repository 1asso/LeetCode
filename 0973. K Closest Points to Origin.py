class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for p in points:
            heappush(heap, (p[0] * p[0] + p[1] * p[1], p))
        for i in range(k):
            res.append(heappop(heap)[1])
        return res
