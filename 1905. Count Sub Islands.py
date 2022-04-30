class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n and grid2[x][y]):
                return True
            grid2[x][y] = 0
            res = grid1[x][y]
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                res &= dfs(x + dx, y + dy) 
            return res 
        count = 0
        return sum(dfs(i, j) for i in range(m) for j in range(n) if grid2[i][j])