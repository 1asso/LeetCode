class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def next_move(x, y):
            for nx, ny in [[x, y + 1], [x, y - 1], [x + 1, y], [x - 1, y]]:
                if 0 <= nx < n and 0 <= ny < n:
                    yield nx, ny
            
        areas = {0: 0}
        index = 2
        def dfs(x, y):
            grid[x][y] = index
            area = 1
            for nx, ny in next_move(x, y):
                if grid[nx][ny] == 1:
                    area += dfs(nx, ny)
            return area
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areas[index] = dfs(i, j)
                    index += 1
        
        max_area = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    s = set(grid[nx][ny] for nx, ny in next_move(i, j))
                    max_area = max(max_area, 1 + sum(areas[x] for x in s))
        return max_area if max_area else max(areas.values())