class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def next_move(x, y):
            for nx, ny in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]:
                    yield nx, ny

        def dfs(x, y, seen):
            seen.add((x, y))
            for nx, ny in next_move(x, y):
                if (nx, ny) not in seen:
                    dfs(nx, ny, seen)
        
        res = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in seen:
                    res += 1
                    dfs(i, j, seen)
        if res != 1:
            return 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    res = 0
                    seen = set()
                    for x in range(m):
                        for y in range(n):
                            if grid[x][y] and (x, y) not in seen:
                                res += 1
                                dfs(x, y, seen)
                    if res != 1:
                        return 1
                    grid[i][j] = 1
        return 2