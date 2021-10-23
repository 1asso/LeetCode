class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = -(p[0] * p[0] + p[1] * p[1])
            if len(heap) == k:
                heappushpop(heap, (dist, p))
            else:
                heappush(heap, (dist, p))
        return [p for dist, p in heap]
