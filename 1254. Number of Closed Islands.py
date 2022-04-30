class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y]:
                return
            grid[x][y] = 1
            for xx, yy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                dfs(xx, yy)
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    dfs(i, j)
        res = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    res += 1
                    dfs(i, j)
        return res