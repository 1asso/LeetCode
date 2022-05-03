Similar to 1-D, use min-heap instead of two pointers:

import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []
        visited = set()
        m, n = len(heightMap), len(heightMap[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))
        res = 0
        while len(visited) < m * n:
            height, i, j = heapq.heappop(heap)
            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    visited.add((x, y))
                    res += max(height - heightMap[x][y], 0)
                    heapq.heappush(heap, (max(height, heightMap[x][y]), x, y))
        return res